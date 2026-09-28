"""Render the captured public Yuque pages as MyST; never execute tutorial code.

Run with the documentation virtualenv (BeautifulSoup is a theme dependency).
Input snapshots contain rendered DOM content, not a Yuque source export.
"""
from pathlib import Path
from urllib.parse import urlsplit, parse_qs
from html import escape
import hashlib
import json
import re

from bs4 import BeautifulSoup, NavigableString
from localize_images import localize_images

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / 'tools/yuque-snapshots'
SOURCE = ROOT / 'source'
PAGES = {
    'dhberyv5btq9hhv1': 'unboxing',
    'nyk0n5c9brbh2l4a': 'pro-quickstart',
    'wgx9twozktvwssu3': 'developer-manual',
    'cyrmk57grrm79vgo': 'faq',
    'phx3zdv7indeo98e': 'troubleshooting',
    'kqoe86xa8ghhw9de': 'advanced',
    'iu44v3gppmu2s9er': 'resources',
    'qd6nueck4cnf2mlq': 'accessories',
    'rp5dnig43ng6uop7': 'product',
    'yyac5sfw94onthd0': 'product-en',
    'us0tnge3dszgxb69': 'education',
    'ixkt9xrygz0zv9b6': 'education-k12',
    'km9oz425a6h1307w': 'videos',
}
ASSETS = json.loads((SNAP / 'assets.json').read_text())
NOTES = {
    'pro-quickstart': '适用型号：AlohaMini 2 Pro。树莓派与 PC 均使用 `alohamini2pro`。相机名称以实际配置为准，采集、转换、训练与推理必须使用一致的数据特征名。IP、设备序列号和检查点路径需替换为本机值。AM-ACT 参数配置见 [训练说明](../training.md)。',
    'developer-manual': '本手册介绍 SO-ARM 与 AM-ARM。AlohaMini 2 / 2 Pro 的机械臂舵机编号为 1–7，底盘为 8–10，升降为 11。请先确认硬件型号，再选择对应的设备配置和 [调试方法](../debug-tools.md)。',
    'faq': '更新软件前，请先保存本机配置和未提交的改动。网络代理地址应替换为自己的服务器地址。',
    'troubleshooting': '按供电、接线、串口和配置顺序排查。完整流程见 [整机排错](../support.md)。',
}



def link(url):
    parsed = urlsplit(url)
    slug = parsed.path.rstrip('/').split('/')[-1]
    if parsed.netloc == 'alohamini.yuque.com' and slug in PAGES:
        return PAGES[slug] + '.md' + ('#yq-' + slug + '-' + parsed.fragment if parsed.fragment else '')
    return url


def render_page(slug):
    data = json.loads((SNAP / f'{slug}.json').read_text())
    assert '[Truncated]' not in data['html'], slug
    soup = BeautifulSoup(data['html'], 'html.parser')
    code_file = SNAP / f'{slug}.codes.json'
    codes = json.loads(code_file.read_text()) if code_file.exists() else {}
    observed = [x['data-code-id'] for x in soup.select('pre[data-code-id]')]
    assert set(observed) == set(codes), (slug, observed, list(codes))
    name = PAGES[slug]
    image_count = 0
    code_count = 0
    video_count = 0
    notes = []
    heading_stack = []

    def inline(node):
        if isinstance(node, NavigableString):
            return str(node).replace('\u200b', '')
        tag = node.name
        content = ''.join(inline(c) for c in node.children)
        if tag == 'a':
            return f'[{content or node.get("href", "链接")}]({link(node.get("href", ""))})'
        if tag in ('ne-code', 'code'):
            return '`' + content + '`'
        if node.get('ne-bold') == 'true' and content.strip():
            return '**' + content.strip() + '**'
        if node.get('ne-italic') == 'true' and content.strip():
            return '*' + content.strip() + '*'
        if tag == 'br':
            return '<br>'
        if tag == 'img':
            return image(node)
        return content.replace('****', '')

    def image(node):
        nonlocal image_count
        url = node.get('src', '')
        if not url or url.startswith('data:'):
            return ''  # Inline bookmark icons are UI decoration.
        if url not in ASSETS:
            raise ValueError(f'{slug}: unarchived image {url}')
        image_count += 1
        src = '../' + ASSETS[url]['path']
        label = node.get('alt') or f'{data["title"]} · 图 {image_count}'
        angle = re.search(r'rotate\((90|270)deg\)', node.get('style', ''))
        if angle:
            # Preserve the rotation used by the source reader; no bitmap edits.
            from PIL import Image
            with Image.open(SOURCE / ASSETS[url]['path']) as im:
                width, height = im.size
            return f'\n\n```{{raw}} html\n<div class="yq-rotated-image" style="aspect-ratio:{height}/{width}"><img src="{escape(src)}" alt="{escape(label)}" style="width:{width/height*100:.4f}%;transform:translate(-50%,-50%) rotate({angle[1]}deg)"></div>\n```\n\n'
        return f'\n\n![{label}]({src})\n\n'

    def block(node):
        nonlocal code_count, video_count
        if isinstance(node, NavigableString):
            return str(node).replace('\u200b', '')
        tag = node.name
        anchor = f'\n\n(yq-{slug}-{node["id"]})=\n\n' if node.get('id') else ''
        if tag == 'pre':
            code_count += 1
            record = codes[node['data-code-id']]
            assert record['text'].strip() and not record['gaps'], (slug, node['data-code-id'])
            language = record.get('language') or 'text'
            if language not in ('bash', 'python', 'json'):
                language = 'text'
            # Keep unmodified commands in the archived Markdown snapshot.
            return anchor + '\n\n```' + language + '\n' + record['text'].rstrip() + '\n```\n\n'
        if tag == 'ne-card':
            kind = node.get('data-card-name')
            if kind == 'image':
                return anchor + ''.join(image(i) for i in node.select('img'))
            if kind == 'hr':
                return '\n\n---\n\n'
            if kind == 'thirdparty':
                frame = node.select_one('iframe')
                url = (frame.get('data-src') or frame.get('src')) if frame else None
                assert url, (slug, node.get('id'))
                bvid = parse_qs(urlsplit(url).query).get('bvid', [None])[0]
                target = f'https://www.bilibili.com/video/{bvid}/' if bvid else url
                if bvid:
                    video_count += 1
                    loading = 'eager' if video_count == 1 else 'lazy'
                    player = f'https://player.bilibili.com/player.html?bvid={bvid}&page=1&autoplay=0'
                    title = f'{data["title"]} · Bilibili 视频 {bvid}'
                    return anchor + (
                        '\n\n```{raw} html\n'
                        '<div class="am-video-embed">'
                        f'<iframe src="{escape(player, quote=True)}" '
                        f'title="{escape(title, quote=True)}" loading="{loading}" '
                        'allow="fullscreen; picture-in-picture" allowfullscreen '
                        'referrerpolicy="strict-origin-when-cross-origin"></iframe>'
                        '</div>\n```\n\n'
                        f'[前往 Bilibili 观看 ↗]({target})\n\n'
                    )
                return anchor + f'\n\n[观看视频 ↗]({target})\n\n'
            if kind == 'video':
                return anchor + f'\n\n[在语雀原文播放本段视频]({data["url"]}#{node.get("id", "")})\n\n'
            if kind == 'file':
                item = json.loads((SNAP / 'attachments.json').read_text())[0]
                return anchor + f'\n\n[{item["title"]}（454 kB，需登录语雀下载）]({item["url"]})\n\n'
            if kind == 'bookmarkInline':
                return inline(node)
            raise ValueError(f'Unsupported card {kind} in {slug}')
        if tag == 'img':
            return image(node)
        if re.fullmatch(r'ne-h[1-6]', tag):
            source_level = int(tag[-1])
            while heading_stack and heading_stack[-1] >= source_level:
                heading_stack.pop()
            heading_stack.append(source_level)
            level = min(6, len(heading_stack) + 1)
            return anchor + '\n\n' + '#' * level + ' ' + inline(node).strip().strip('*') + '\n\n'
        if tag in ('ne-uli', 'ne-oli'):
            return anchor + '\n' + ('1. ' if tag == 'ne-oli' else '- ') + inline(node).strip() + '\n'
        if tag == 'ne-quote':
            return anchor + '\n\n' + '\n'.join('> ' + l for l in ''.join(block(c) for c in node.children).strip().splitlines()) + '\n\n'
        if tag == 'table':
            # Markdown tables preserve all cell text; expand merged cells across rows.
            grid = []; spans = {}
            for row in node.select('tr'):
                cells = []; col = 0
                for cell in row.find_all(['td', 'th'], recursive=False):
                    while col in spans:
                        value, left = spans.pop(col); cells.append(value)
                        if left > 1: spans[col] = (value, left - 1)
                        col += 1
                    value = inline(cell).strip().replace('\n', ' ').replace('|', '\\|')
                    for _ in range(int(cell.get('colspan', 1))):
                        cells.append(value)
                        if int(cell.get('rowspan', 1)) > 1: spans[col] = (value, int(cell['rowspan']) - 1)
                        col += 1
                while col in spans:
                    value, left = spans.pop(col); cells.append(value)
                    if left > 1: spans[col] = (value, left - 1)
                    col += 1
                grid.append(cells)
            if not grid: return ''
            width = max(map(len, grid)); grid = [r + [''] * (width-len(r)) for r in grid]
            lines = ['| ' + ' | '.join(r) + ' |' for r in grid]
            return anchor + '\n\n' + '\n'.join([lines[0], '| ' + ' | '.join(['---']*width) + ' |'] + lines[1:]) + '\n\n'
        if tag == 'ne-p':
            # Cards can occur inside paragraphs; process them as blocks.
            return anchor + '\n\n' + ''.join(block(c) if getattr(c, 'name', '') == 'ne-card' else inline(c) for c in node.children).strip() + '\n\n'
        return anchor + ''.join(block(c) for c in node.children)

    body = ''.join(block(c) for c in soup.children)
    body = re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'
    original = f'# {data["title"]}\n\n来源：{data["url"]}\n网页读取日期：2026-09-28。此文件为公开页面转写，并非语雀原生 Markdown 导出。\n\n' + body
    archive = SOURCE / '_static/yuque-originals' / f'{name}.md.txt'
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text(original)
    edits = []
    embedded_bvids = {
        parse_qs(urlsplit(frame.get('data-src') or frame.get('src', '')).query).get('bvid', [''])[0]
        for frame in soup.select('iframe')
    } - {''}
    cleaned_lines = []
    for line in body.splitlines():
        raw_link = re.fullmatch(r'\[(https://player\.bilibili\.com/[^\]]+)\]\(([^)]+)\)', line)
        if raw_link:
            bvid = parse_qs(urlsplit(raw_link[2]).query).get('bvid', [''])[0]
            if bvid in embedded_bvids:
                edits.append('移除已嵌入视频的重复播放器网址，保留 Bilibili 观看入口')
                continue
        cleaned_lines.append(line)
    body = '\n'.join(cleaned_lines) + '\n'
    if name == 'videos':
        for node_id, filename, title in (
            ('dtxAU', 'knews.mp4', '看看新闻 Knews'),
            ('TeJuG', 'moduyan.mp4', '魔都眼'),
        ):
            asset = SOURCE / '_static/yuque-videos' / filename
            assert asset.is_file(), asset
            original_link = f'[在语雀原文播放本段视频]({data["url"]}#{node_id})'
            assert original_link in body, node_id
            player = (
                '```{raw} html\n'
                f'<video class="am-local-video" controls playsinline preload="metadata" '
                f'aria-label="{title}" src="../_static/yuque-videos/{filename}">'
                f'您的浏览器不支持视频播放。<a href="../_static/yuque-videos/{filename}">下载视频</a>'
                '</video>\n```'
            )
            body = body.replace(original_link, player)
    if name in ('pro-quickstart', 'developer-manual'):
        body = re.sub(r'--robot\.robot_model alohamini2(?=\s|$)', '--robot.robot_model alohamini2pro', body)
        edits.append('统一 Pro Host 与 PC 的 robot_model')
    if name == 'pro-quickstart':
        body = body.replace('python examples/alohamini/calibrate_bi.py \n--teleop.id am_leader_bi \n--teleop.arm_profile am-leader-6dof', 'python examples/alohamini/calibrate_bi.py \\\n  --teleop.id am_leader_bi \\\n  --teleop.arm_profile am-leader-6dof')
        edits.append('补齐 calibrate_bi 命令续行符')
    if name == 'developer-manual':
        body = body.replace('liyitenga/lerobot_alohamini', 'liyiteng/lerobot_alohamini')
        old = codes['eIB1v']['text'].rstrip()
        new = 'conda activate lerobot_alohamini\ncd lerobot_alohamini\n# 将 IP 替换为本机地址；本段示例适用于 2 Pro\npython examples/alohamini/teleoperate_bi.py \\\n  --robot.remote_ip 192.168.50.88 \\\n  --robot.robot_model alohamini2pro \\\n  --teleop.id am_leader_bi \\\n  --teleop.arm_profile am-leader-6dof'
        body = body.replace(old, new)
        edits += ['修正仓库用户名拼写', '将旧式遥操作参数更新为嵌套参数，并移除续行符后的行尾注释']
    if name == 'faq':
        body = body.replace('1、还原工作区', '1、检查并保存本地改动').replace('git restore .', '`git status`：先查看差异，保存你的配置和校准相关改动；存在未处理改动时先完成备份或提交。').replace('git pull', 'git pull --ff-only').replace('3、正常应当显示Already up to date', '3、没有新提交时会显示 Already up to date；有更新时会列出变动。发生冲突或无法快进时，先处理分支差异。')
        edits.append('用保留本地改动的更新步骤替换 git restore .')
    if name == 'troubleshooting':
        body = body.replace('lerobot.robots.alohamini.lekiwi host', 'lerobot.robots.alohamini.alohamini_host')
        edits.append('修正 Host 模块名拼写')
    body = body.replace('需登录语雀下载', '需登录下载')
    # Separate punctuation-ending emphasis from Chinese text so MyST renders
    # the labels as bold rather than displaying the Markdown asterisks.
    body = re.sub(r'\*\*([^*\n]+[：:])\*\*(?=\S)', r'**\1** ', body)
    body = body.replace('**全栈生态适配：：**', '**全栈生态适配：**')
    intro = NOTES.get(name, '')
    page = SOURCE / 'yuque' / f'{name}.md'
    page.parent.mkdir(exist_ok=True)
    note = f'{intro}\n\n' if intro else ''
    page.write_text(localize_images(f'# {data["title"]}\n\n[返回官方使用手册](../official-manual.md)\n\n' + note + body, page))
    return {'title': data['title'], 'url': data['url'], 'page': f'yuque/{name}.md', 'images': image_count, 'code_blocks': code_count, 'corrections': edits, 'snapshot_sha256': hashlib.sha256((SNAP/f'{slug}.json').read_bytes()).hexdigest(), 'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}


def main():
    entries = [render_page(slug) for slug in PAGES]
    manifest = {'captured_on': '2026-09-28', 'method': 'Public rendered DOM; code blocks captured individually after loading. No API token.', 'sources': entries, 'assets': ASSETS, 'attachments': json.loads((SNAP/'attachments.json').read_text())}
    (ROOT / 'yuque-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    print(f'{len(entries)} pages; {sum(e["code_blocks"] for e in entries)} code blocks; {sum(e["images"] for e in entries)} image references')


if __name__ == '__main__':
    main()
