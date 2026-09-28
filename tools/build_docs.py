"""Build both languages with matching page paths and original section anchors."""
import argparse
import hashlib
import os
import re
import shutil
from urllib.parse import urlsplit, urlunsplit
import json
import pickle
from pathlib import Path
import subprocess
import sys
from docutils import nodes

ROOT = Path(__file__).resolve().parents[1]


def share_media(output):
    """Keep one copy of language-independent media in the published site."""
    english = output / 'en'
    folders = ['_images'] + ['_static/' + name for name in (
        'media', 'external-images', 'upstream-assets', 'upstream-originals',
        'upstream-licenses', 'yuque-assets', 'yuque-originals', 'yuque-videos')]
    shared = {}
    for folder in folders:
        for path in (english / folder).rglob('*'):
            if not path.is_file():
                continue
            target = output / path.relative_to(english)
            if not target.is_file() or hashlib.sha256(path.read_bytes()).digest() != hashlib.sha256(target.read_bytes()).digest():
                raise RuntimeError(f'Media differs between languages: {path}')
            shared[path.resolve()] = target
    for page in english.rglob('*.html'):
        def rewrite(match):
            url = urlsplit(match[2])
            if url.scheme or url.netloc:
                return match[0]
            target = shared.get((page.parent / url.path).resolve())
            if target is None:
                return match[0]
            relative = os.path.relpath(target, page.parent).replace(os.sep, '/')
            return match[1] + urlunsplit(('', '', relative, url.query, url.fragment)) + match[3]
        text = re.sub(r'((?:src|href|poster)=["\'])([^"\']+)(["\'])', rewrite, page.read_text())
        page.write_text(text)
    for folder in folders:
        directory = english / folder
        if directory.exists():
            shutil.rmtree(directory)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', default='')
    args = parser.parse_args()
    output = ROOT / 'build/html'
    anchors = ROOT / 'build/language-anchors.json'
    for language, destination in [('zh_CN', output), ('en', output / 'en')]:
        doctrees = ROOT / 'build/doctrees' / language
        command = [sys.executable, '-m', 'sphinx', '-E', '-W', '--keep-going', '-b', 'html',
                   '-d', str(doctrees),
                   '-D', f'language={language}']
        if args.base_url:
            base = args.base_url.rstrip('/') + ('/en/' if language == 'en' else '/')
            command += ['-D', f'html_baseurl={base}']
        if language == 'en':
            command += ['-D', f'am_anchor_manifest={anchors}']
        command += [str(ROOT / 'source'), str(destination)]
        subprocess.run(command, check=True, cwd=ROOT)
        if language == 'zh_CN':
            # Read only doctrees generated above by this local build.
            env = pickle.loads((doctrees / 'environment.pickle').read_bytes())
            mapping = {}
            for name in sorted(env.found_docs):
                doc = pickle.loads((doctrees / (name + '.doctree')).read_bytes())
                mapping[name] = {
                    'ids': [section['ids'] for section in doc.findall(nodes.section)],
                    'slugs': env.metadata.get(name, {}).get('myst_slugs', {}),
                }
            anchors.write_text(json.dumps(mapping, ensure_ascii=False))
    share_media(output)
    # Remove obsolete generated caches from builds made before -d was set.
    for old_cache in (output / '.doctrees', output / 'en/.doctrees'):
        if old_cache.is_dir():
            shutil.rmtree(old_cache)


if __name__ == '__main__':
    main()
