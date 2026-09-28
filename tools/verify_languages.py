"""Check translation coverage, unchanged commands, and reciprocal language links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / 'build/html'
CJK = re.compile(r'[\u4e00-\u9fff]')


def code_blocks(text):
    blocks = []
    fence = None
    for line in text.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})(.*)', line)
        if match:
            if fence and match[1][0] == fence[0] and len(match[1]) >= len(fence):
                if not directive:
                    blocks.append('\n'.join(body))
                fence = None
            elif fence is None:
                fence = match[1]
                directive = match[2].startswith('{')
                body = [match[2]]
        elif fence:
            body.append(line)
    return blocks


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.lang = None
        self.switches = []
        self.article = 0
        self.skip = 0
        self.body = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'a' and 'am-language-switcher' in attrs.get('class', '').split():
            self.switches.append(attrs['href'])
        if tag == 'article':
            self.article += 1
        if tag in ('pre', 'code', 'script', 'style'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag == 'article':
            self.article -= 1
        if tag in ('pre', 'code', 'script', 'style'):
            self.skip -= 1

    def handle_data(self, text):
        if self.article and not self.skip:
            self.body.append(text)


def main():
    errors = []
    sources = [p for p in (ROOT / 'source').rglob('*.md') if '_static' not in p.parts]
    for source in sources:
        relative = source.relative_to(ROOT / 'source')
        translated = ROOT / 'translations/en' / relative
        if not translated.is_file():
            errors.append(f'Missing translation: {relative}')
            continue
        if code_blocks(source.read_text()) != code_blocks(translated.read_text()):
            errors.append(f'Executable code changed: {relative}')
    for zh_path in HTML.rglob('*.html'):
        relative = zh_path.relative_to(HTML)
        if relative.parts[0] in ('en', '_static'):
            continue
        en_path = HTML / 'en' / relative
        if not en_path.exists():
            errors.append(f'Missing English HTML: {relative}')
            continue
        for path, expected, other in [(zh_path, 'zh-CN', en_path), (en_path, 'en', zh_path)]:
            doc = Document(path)
            if doc.lang != expected:
                errors.append(f'{path.relative_to(HTML)}: lang={doc.lang}, expected {expected}')
            if not doc.switches:
                errors.append(f'Missing language switch: {path.relative_to(HTML)}')
            for link in doc.switches:
                target = (path.parent / unquote(urlsplit(link).path)).resolve()
                if target != other.resolve():
                    errors.append(f'Wrong language target: {path.relative_to(HTML)} -> {link}')
            if expected == 'en':
                untranslated = [text.strip() for text in doc.body if CJK.search(text)]
                if untranslated:
                    errors.append(f'Chinese prose in {path.relative_to(HTML)}: {untranslated[:3]}')
    print(f'{len(sources)} translation pairs; {len(errors)} language errors')
    for error in errors:
        print(error)
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
