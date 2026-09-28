"""Cache images referenced by built pages, then rewrite Markdown to local paths.

Run after sphinx-build: python3 tools/localize_images.py --download
Without --download, only apply the existing offline manifest. Original archives
and video embeds are never rewritten. Badges become snapshots at download time.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
from html import escape
import io
import json
import os
from pathlib import Path
import subprocess
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'source'
MANIFEST = ROOT / 'external-images.json'


def read_manifest():
    return json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {'images': {}, 'failures': {}}


def localize_images(text, page, manifest=None):
    manifest = manifest if manifest is not None else read_manifest()
    for url, item in sorted(manifest['images'].items(), key=lambda pair: -len(pair[0])):
        relative = Path(os.path.relpath(SOURCE / item['path'], Path(page).parent)).as_posix()
        # Sphinx normalizes spaces in URLs; raw HTML may escape ampersands.
        for variant in {url, unquote(url), url.replace('%20', ' ')}:
            text = text.replace(escape(variant, quote=True), relative).replace(variant, relative)
    return text


def discover():
    refs = {}
    for page in (ROOT / 'build/html').rglob('*.html'):
        if '_static' in page.relative_to(ROOT / 'build/html').parts:
            continue
        soup = BeautifulSoup(page.read_text(), 'html.parser')
        for img in soup.select('img[src], video[poster]'):
            url = img.get('src') if img.name == 'img' else img.get('poster')
            if urlsplit(url).netloc:
                if url.startswith('//'):
                    url = 'https:' + url
                refs.setdefault(url, set()).add(str(page.relative_to(ROOT / 'build/html')))
    return refs


def download(url, pages):
    from PIL import Image
    # The upstream gamepad chart is 233 MP. Inspect headers without decoding or
    # resizing its pixels, while retaining a finite limit for unexpected files.
    Image.MAX_IMAGE_PIXELS = 250_000_000
    result = subprocess.run(
        ['curl', '--http1.1', '--fail', '--location', '--silent', '--show-error',
         '--connect-timeout', '15', '--max-time', '90', '--retry', '1',
         '--max-filesize', '90000000', url], capture_output=True, check=True)
    data = result.stdout
    if len(data) > 90_000_000:
        raise ValueError('Image exceeds 90 MB')
    try:
        root = ET.fromstring(data)
        if root.tag.rsplit('}', 1)[-1] != 'svg':
            raise ValueError('Not an SVG image')
        extension = 'svg'
    except ET.ParseError:
        with Image.open(io.BytesIO(data)) as image:
            extension = {'JPEG': 'jpg', 'PNG': 'png', 'GIF': 'gif', 'WEBP': 'webp', 'AVIF': 'avif'}[image.format]
            image.verify()
    digest = hashlib.sha256(data).hexdigest()
    relative = f'_static/external-images/{digest[:20]}.{extension}'
    target = SOURCE / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return {'path': relative, 'sha256': digest, 'bytes': len(data),
            'downloaded_at': datetime.now(timezone.utc).isoformat(), 'pages': sorted(pages)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--download', action='store_true')
    args = parser.parse_args()
    manifest = read_manifest()
    if args.download:
        refs = discover()
        for url, item in manifest['images'].items():
            refs.setdefault(url, set(item['pages']))
        pending = {url: pages for url, pages in refs.items() if url not in manifest['images']}
        with ThreadPoolExecutor(max_workers=6) as pool:
            futures = {pool.submit(download, url, pages): url for url, pages in pending.items()}
            for future in as_completed(futures):
                url = futures[future]
                try:
                    item = future.result()
                    manifest['images'][url] = item
                    manifest['failures'].pop(url, None)
                    print(f'OK {item["bytes"]:,} bytes: {url}', flush=True)
                except Exception as error:
                    detail = error.stderr.decode(errors='replace') if isinstance(error, subprocess.CalledProcessError) else str(error)
                    manifest['failures'][url] = detail.strip()
                    print(f'FAILED: {url}: {detail.strip()}', flush=True)
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    changed = 0
    for page in SOURCE.rglob('*.md'):
        if '_static' in page.relative_to(SOURCE).parts:
            continue
        before = page.read_text()
        after = localize_images(before, page, manifest)
        if before != after:
            page.write_text(after)
            changed += 1
    print(f'{len(manifest["images"])} cached URLs; {len(manifest["failures"])} failures; {changed} pages updated')


if __name__ == '__main__':
    main()
