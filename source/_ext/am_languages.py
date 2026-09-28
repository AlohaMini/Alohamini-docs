"""Language-specific Markdown with stable page URLs and shared site templates."""
from pathlib import Path
import json
from sphinx.errors import ExtensionError
from docutils import nodes


def configure(app, config):
    english = config.language == 'en'
    config.html_title = 'AlohaMini Documentation' if english else 'AlohaMini 文档'
    config.html_search_language = 'en' if english else 'zh'
    config.html_theme_options['search_bar_text'] = 'Search documentation…' if english else '搜索文档…'
    config.html_context['am_english'] = english
    if english:
        labels = json.loads((Path(app.confdir).parent / 'translations/en/navigation.json').read_text())
        config.html_context['navigation_groups'] = [
            (labels[title], [(page, labels[label], icon) for page, label, icon in pages])
            for title, pages in config.html_context['navigation_groups']
        ]


def read_translation(app, docname, source):
    if app.config.language != 'en':
        return
    translated = Path(app.confdir).parent / 'translations/en' / (docname + '.md')
    if not translated.exists():
        raise ExtensionError(f'Missing English translation: {translated}')
    app.env.note_dependency(str(translated))
    source[0] = translated.read_text()


def preserve_anchors(app, doctree):
    if app.config.language != 'en':
        return
    manifest = Path(app.config.am_anchor_manifest)
    if not manifest.is_file():
        raise ExtensionError('Build both languages with python tools/build_docs.py')
    data = json.loads(manifest.read_text())[app.env.docname]
    sections = list(doctree.findall(nodes.section))
    if len(sections) != len(data['ids']):
        raise ExtensionError(f'Heading structure differs in translation: {app.env.docname}')
    original_ids = {identifier for group in data['ids'] for identifier in group}
    english_targets = {}
    for section, identifiers in zip(sections, data['ids']):
        for identifier in section['ids']:
            english_targets[identifier] = identifiers[0]
            if doctree.ids.get(identifier) is section:
                del doctree.ids[identifier]
    for section, identifiers in zip(sections, data['ids']):
        # Original IDs are canonical. Keep translated IDs as extra aliases only
        # when they cannot collide with a different original section.
        aliases = [identifier for identifier in section['ids'] if identifier not in original_ids]
        section['ids'] = list(identifiers) + aliases
        for identifier in section['ids']:
            doctree.ids[identifier] = section
    slugs = app.env.metadata.setdefault(app.env.docname, {}).setdefault('myst_slugs', {})
    for slug, (line, target, title) in list(slugs.items()):
        slugs[slug] = (line, english_targets.get(target, target), title)
    for slug, target in data['slugs'].items():
        slugs.setdefault(slug, target)


def page_context(app, pagename, templatename, context, doctree):
    english = app.config.language == 'en'
    if pagename in {'index', 'quickstart', 'official-manual', 'alohamini2', 'alohamini2pro'}:
        context['theme_show_prev_next'] = False
    root = '../' * pagename.count('/')
    context['am_other_language_url'] = root + ('../' if english else 'en/') + pagename + '.html'
    context['am_language_label'] = 'Language' if english else '语言'
    context['am_other_language'] = '简体中文' if english else 'English'
    context['am_anchor_map'] = {}
    if english and doctree is not None:
        manifest = json.loads(Path(app.config.am_anchor_manifest).read_text())
        original = manifest[pagename]['ids']
        for section, identifiers in zip(doctree.findall(nodes.section), original):
            if identifiers:
                for identifier in section['ids']:
                    context['am_anchor_map'][identifier] = identifiers[0]


def setup(app):
    app.add_config_value('am_anchor_manifest', '', 'env')
    app.connect('config-inited', configure)
    app.connect('doctree-read', preserve_anchors)
    app.connect('source-read', read_translation)
    app.connect('html-page-context', page_context)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
