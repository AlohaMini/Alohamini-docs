"""Verify imported source integrity and generated local links after sphinx-build."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'source'
HTML = ROOT / 'build/html'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.text = []
        self.external_images = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        image_url = values.get('src') if tag == 'img' else values.get('poster') if tag == 'video' else None
        if image_url and urlsplit(image_url).netloc:
            self.external_images.append(image_url)
        if 'id' in values:
            self.ids.add(values['id'])
        for key in ('href', 'src', 'poster'):
            if key in values:
                self.links.append(values[key])

    def handle_data(self, data):
        self.text.append(data)


def main():
    errors = []
    manifest = json.loads((ROOT / 'upstream-manifest.json').read_text())
    for entry in manifest['sources']:
        path = SOURCE / '_static/upstream-originals' / entry['kind'] / (entry['path'] + '.txt')
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
            errors.append(f'Original changed or missing: {path}')
        page = SOURCE / entry['page']
        if not page.exists() or not (HTML / entry['page']).with_suffix('.html').exists():
            errors.append(f'Missing rendered document: {entry["page"]}')
    for alias in manifest['aliases']:
        if not (SOURCE / alias['page']).exists():
            errors.append(f'Unresolved alias: {alias["path"]}')
    yuque_path = ROOT / 'yuque-manifest.json'
    if yuque_path.exists():
        yuque = json.loads(yuque_path.read_text())
        snapshots = ROOT / 'tools/yuque-snapshots'
        expected = {entry['url'] for entry in json.loads((snapshots / 'index.json').read_text())}
        if expected != {entry['url'] for entry in yuque['sources']}:
            errors.append('Yuque directory and imported pages do not match')
        for entry in yuque['sources']:
            slug = entry['url'].rstrip('/').split('/')[-1]
            snapshot = snapshots / f'{slug}.json'
            archive = SOURCE / '_static/yuque-originals' / (Path(entry['page']).stem + '.md.txt')
            for path, checksum in ((snapshot, entry['snapshot_sha256']), (archive, entry['archive_sha256'])):
                if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != checksum:
                    errors.append(f'Yuque content changed or missing: {path}')
            if not (HTML / entry['page']).with_suffix('.html').exists():
                errors.append(f'Missing Yuque page: {entry["page"]}')
            codes_path = snapshots / f'{slug}.codes.json'
            if codes_path.exists():
                codes = json.loads(codes_path.read_text())
                if len(codes) != entry['code_blocks']:
                    errors.append(f'Yuque code count mismatch: {slug}')
                for code_id, code in codes.items():
                    if code['gaps'] or not code['text'].strip() or code['text'].rstrip() not in archive.read_text():
                        errors.append(f'Incomplete archived code: {slug}/{code_id}')
        for asset in yuque['assets'].values():
            path = SOURCE / asset['path']
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != asset['sha256']:
                errors.append(f'Yuque image changed or missing: {path}')
        print(f'Yuque: {len(yuque["sources"])} pages; {sum(e["code_blocks"] for e in yuque["sources"])} archived code blocks; {len(yuque["assets"])} image URLs verified')
    pages = {p: Page(p.read_text()) for p in HTML.rglob('*.html') if '_static' not in p.relative_to(HTML).parts}
    image_manifest = ROOT / 'external-images.json'
    if image_manifest.exists():
        images = json.loads(image_manifest.read_text())
        for url, item in images['images'].items():
            path = SOURCE / item['path']
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
                errors.append(f'Cached image changed or missing: {url}')
        for path, page in pages.items():
            for url in page.external_images:
                errors.append(f'{path.relative_to(HTML)}: image still uses an external URL: {url}')
        print(f'External image cache: {len(images["images"])} URLs verified')
    if not pages:
        errors.append('No HTML pages; build the site first.')
    for path, page in pages.items():
        public_text = ''.join(page.text)
        for phrase in ('语雀', '本页保留', '项目参考：', '来源转写与核对', '上游完整命令'):
            if phrase in public_text:
                errors.append(f'{path.relative_to(HTML)}: internal editorial text is visible: {phrase}')
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target /= 'index.html'
            if not target.exists():
                errors.append(f'{path.relative_to(HTML)}: missing {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(HTML)}: missing anchor {link}')
    print(f'{len(manifest["sources"])} original checksums; {len(manifest["aliases"])} aliases; {len(pages)} HTML pages; {len(errors)} errors')
    for error in errors:
        print(error)
    raise SystemExit(bool(errors))

if __name__ == '__main__':
    main()
