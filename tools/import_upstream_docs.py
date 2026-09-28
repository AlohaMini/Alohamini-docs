"""Import pinned, local Git objects as readable reference pages and exact downloads.

Run with: python tools/import_upstream_docs.py --hardware ../AlohaMini --software ../lerobot_alohamini
Only reads the upstream repositories; never executes their examples or fetches assets.
"""
import argparse
import hashlib
import json
import posixpath
import re
import subprocess
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from localize_images import localize_images

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'source'
REPOS = {
    'hardware': ('liyiteng/AlohaMini', '17c6a98d79881a45ab869c1f392ed89c0723a298'),
    'software': ('liyiteng/lerobot_alohamini', '7843e5888366eaa553630e2f9d5539505a62dddf'),
}
EXCLUDED = {'AGENTS.md', 'CLAUDE.md', 'AI_POLICY.md', 'CODE_OF_CONDUCT.md', 'SECURITY.md', '.github/PULL_REQUEST_TEMPLATE.md',
 'src/lerobot/datasets/card_template.md', 'src/lerobot/templates/lerobot_modelcard_template.md', 'src/lerobot/templates/lerobot_rewardmodel_modelcard_template.md'}
POLICIES = set('act diffusion eo1 evo1 fastwam groot lingbot_va molmoact2 multi_task_dit pi0 pi05 pi0fast rtc sarm smolvla tdmpc vla_jepa vqbet walloss xvla'.split())
DATA = set('annotation_pipeline lerobot-dataset-v3 porting_datasets_v3 using_dataset_tools streaming_video_encoding video_encoding_parameters rename_map language_and_recipes action_representations'.split())
DEV = set('adding_benchmarks bring_your_own_policies processors_robots_teleop debug_processor_pipeline implement_your_own_processor env_processor introduction_processors integrate_hardware backwardcomp contributing'.split())
SIM = set('hilserl_sim libero_plus envhub libero robotwin robocasa metaworld vlabench envhub_leisaac robomme envhub_isaaclab_arena'.split())
HARDWARE = set('earthrover_mini_plus rebot_b601 hope_jr openarm lekiwi feetech robocerebra phone_teleop koch damiao so100 so101 unitree_g1 hardware_guide omx reachy2 isaac_teleop cameras'.split())
CATEGORIES = {'alohamini':'AlohaMini 原始教程','policies':'策略与模型','data':'数据集与编码','simulation':'仿真与基准','development':'开发与扩展','environment':'环境与训练工具','hardware':'其他硬件与遥操作'}
TITLES = {'README':'项目说明','AGENT_GUIDE':'LeRobot 使用指南','install':'软件安装','profiles':'硬件配置','alohamini':'整机工作流','am-arm200':'AM-ARM200 工作流','commands':'命令大全','BOM':'物料清单','hardware_assembly':'一代硬件装配','software_setup':'一代软件入口','assembly_guide':'二代硬件装配','print_guide':'二代打印指南'}

def git(repo, *args):
    return subprocess.check_output(['git','-C',str(repo),*args])

def category(kind,path):
    stem=Path(path).stem
    if kind=='hardware' or path.startswith('docs/alohamini/') or path.startswith('examples/debug/'):
        return 'alohamini'
    if path.startswith('alohamini_sim/') or stem in SIM: return 'simulation'
    if '/policies/' in path or stem in POLICIES or stem.startswith('policy_'): return 'policies'
    if stem in DATA: return 'data'
    if stem in DEV or path=='CONTRIBUTING.md': return 'development'
    if stem in HARDWARE or path.startswith('examples/'): return 'hardware'
    return 'environment'

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in REPOS: ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args()
    entries=[]; trees={}; aliases={}; exclusions=[]
    for kind,(repo_name,revision) in REPOS.items():
        repo=getattr(args,kind)
        tree={}
        for record in git(repo,'ls-tree','-rz',revision).split(b'\0'):
            if not record: continue
            meta,path=record.decode().split('\t',1)
            mode,typ,oid=meta.split()
            tree[path]={'mode':mode,'oid':oid}
        trees[kind]=tree
        for path,item in sorted(tree.items()):
            if not path.lower().endswith(('.md','.mdx','.rst')): continue
            if path in EXCLUDED:
                exclusions.append({'repository':repo_name,'path':path,'reason':'仓库治理、代理指令或模板，不属于教程'})
                continue
            if item['mode']=='120000':
                target=git(repo,'show',f'{revision}:{path}').decode().strip()
                aliases[(kind,path)]=posixpath.normpath(posixpath.join(posixpath.dirname(path),target))
                continue
            slug=kind+'--'+re.sub(r'[^a-zA-Z0-9_-]+','-',path.rsplit('.',1)[0]).lower()
            entries.append({'kind':kind,'repository':repo_name,'revision':revision,'path':path,'page':f'upstream/{slug}.md','category':category(kind,path),'sha256':'','assets':[]})
    pages={(e['kind'],e['path']):e['page'] for e in entries}
    for key,target in aliases.items():
        if (key[0],target) not in pages: raise ValueError(f'Unresolved documentation alias: {key}: {target}')
        pages[key]=pages[(key[0],target)]
    (SOURCE/'upstream').mkdir(exist_ok=True)
    for entry in entries:
        kind=entry['kind']; path=entry['path']; rev=entry['revision']; name=entry['repository']; repo=getattr(args,kind)
        original=git(repo,'show',f'{rev}:{path}')
        entry['sha256']=hashlib.sha256(original).hexdigest()
        download=SOURCE/'_static/upstream-originals'/kind/(path+'.txt')
        download.parent.mkdir(parents=True,exist_ok=True);download.write_bytes(original)
        dest=SOURCE/entry['page']
        def rel(p): return posixpath.relpath(str(p),str(dest.parent))
        def resolve(url,asset=False):
            url=url.replace('\\','/')
            if url.startswith(('http:','https:','mailto:','data:','tel:','//')): return url
            if url.startswith('www.') or url.startswith('amazon.com/'): return 'https://'+url
            u=urlsplit(url); target=posixpath.normpath(posixpath.join(posixpath.dirname(path),unquote(u.path))) if u.path else path
            candidates=[target,target+'.mdx',target+'.md',target+'/README.md']
            match=next((x for x in candidates if (kind,x) in pages),None)
            # Original GitHub anchors may not match MyST slugs; keep fragment links at the source.
            if match and not u.fragment and not asset: return rel(SOURCE/pages[(kind,match)])
            if asset and target in trees[kind]:
                size=int(git(repo,'cat-file','-s',trees[kind][target]['oid']))
                if size<=8_000_000:
                    output=SOURCE/'_static/upstream-assets'/kind/target
                    output.parent.mkdir(parents=True,exist_ok=True)
                    if not output.exists(): output.write_bytes(git(repo,'show',f'{rev}:{target}'))
                    entry['assets'].append({'path':target,'status':'local'})
                    return rel(output)
                entry['assets'].append({'path':target,'status':'remote-large'})
            elif asset:
                entry['assets'].append({'path':target,'status':'upstream-missing'})
            base=('https://raw.githubusercontent.com/'+name+'/'+rev+'/') if asset else ('https://github.com/'+name+'/blob/'+rev+'/')
            if not asset and not match and target not in trees[kind]: base='https://github.com/'+name+'/tree/'+rev+'/'
            return base+quote(target,safe='/')+('?' + u.query if u.query else '')+('#'+u.fragment if u.fragment else '')
        body=original.decode('utf-8')
        # Preserve fenced code byte-for-byte; only adapt prose/markup outside fences.
        # Use line-level fence state to also handle malformed upstream closing fences safely.
        output=[]; fence=None; prose=[]
        def convert(chunk):
            chunk=re.sub(r'<hfoption\b[^>]*\bid=["\']([^"\']+)["\'][^>]*>',lambda m:'\n\n**'+m[1]+'**\n\n',chunk,flags=re.I)
            chunk=re.sub(r'</?hfoptions?\b[^>]*>','\n',chunk,flags=re.I)
            chunk=re.sub(r'<Tip\b[^>]*>','\n\n**原文提示**\n\n',chunk)
            chunk=re.sub(r'</Tip>','\n\n',chunk)
            chunk=re.sub(r'</?details\b[^>]*>','\n\n',chunk,flags=re.I)
            chunk=re.sub(r'<summary\b[^>]*>(.*?)</summary>',lambda m:'\n\n**'+re.sub('<[^>]+>','',m[1])+'**\n\n',chunk,flags=re.S|re.I)
            # Component widgets are expressed as links; no third-party scripts are imported.
            chunk=re.sub(r'<Youtube\s+id="([A-Za-z0-9_-]+)"\s*/>', lambda m: "[观看原文视频](https://www.youtube.com/watch?v="+m[1]+")", chunk)
            chunk=re.sub(r'<script\b.*?</script>','',chunk,flags=re.S|re.I)
            chunk=re.sub(r'\[\[autodoc\]\]\s+([^\n]+)',r'**API 参考：`\1`**（接口详情见原文和源码）',chunk)
            chunk=re.sub(r'(!?\[[^\]\n]*\]\()([^\s)]+)([^)\n]*\))',lambda m:m[1]+resolve(m[2],m[1].startswith('!'))+m[3],chunk)
            chunk=re.sub(r'^(\s*\[[^\]]+\]:\s*)(\S+)',lambda m:m[1]+resolve(m[2]),chunk,flags=re.M)
            chunk=re.sub(r'\b(src|href|poster)=("|\')(.*?)\2',lambda m:m[1]+'='+m[2]+resolve(m[3],m[1]!='href')+m[2],chunk,flags=re.S)
            # HF frontmatter anchors, e.g. heading [[anchor]], become plain headings.
            chunk=re.sub(r'^(#{1,6} .*?)\s*\[\[[^\]]+\]\]\s*$',r'\1',chunk,flags=re.M)
            return chunk
        for line in body.splitlines(keepends=True):
            fm=re.match(r'^\s*(`{3,}|~{3,})(.*)',line)
            if fence:
                output.append(line)
                if fm and fm[1][0]==fence[0] and len(fm[1])>=len(fence) and not fm[2].strip(): fence=None
            elif fm:
                output.append(convert(''.join(prose)));prose=[]
                fence=fm[1];output.append(line)
            else: prose.append(line)
        output.append(convert(''.join(prose)))
        converted=''.join(output)
        # Repair the upstream environment-processor document's unclosed nested fence.
        # The source download above remains unchanged; only delimiters are repaired.
        if path == 'docs/source/env_processor.mdx':
            converted = converted.replace('````python', '```python').replace('````', '```')
            converted = converted.replace('act_postprocessor = make_pre_post_processors(act_cfg)\n```python',
                                          'act_postprocessor = make_pre_post_processors(act_cfg)\n```\n\n```python')
            converted = converted.replace('act_postprocessor = make_pre_post_processors(act_cfg)\n\n### 3.',
                                          'act_postprocessor = make_pre_post_processors(act_cfg)\n```\n\n### 3.')
        # Keep upstream title but make each page independently navigable.
        title_match=re.search(r'^# (.+)$',body,re.M)
        title=re.sub('<[^>]+>','',title_match[1]) if title_match else TITLES.get(Path(path).stem,Path(path).stem)
        title=re.sub(r'\s*\[\[.*?\]\]','',title).strip()
        entry['title']=title
        if title_match:
            converted=re.sub(r'^# .+\n','',converted,count=1,flags=re.M)
        # Normalize skipped heading levels and lexer labels without changing code contents.
        formatted=[]; fence=None; stack=[]
        for line in converted.splitlines(keepends=True):
            fm=re.match(r'^\s*(`{3,}|~{3,})(.*)',line)
            if fence:
                formatted.append(line)
                if fm and fm[1][0]==fence[0] and len(fm[1])>=len(fence) and not fm[2].strip(): fence=None
                continue
            if fm:
                fence=fm[1]
                language=fm[2].strip()
                if language in ('udev','bach'):
                    line=line.replace(language, 'text' if language=='udev' else 'bash', 1)
                if path=='docs/source/bring_your_own_policies.mdx' and language=='toml':
                    line=line.replace('toml','text',1)
                formatted.append(line);continue
            hm=re.match(r'^(#{1,6}) (.*)',line)
            if hm:
                original_level=len(hm[1])
                while stack and stack[-1][0]>=original_level: stack.pop()
                level=min((stack[-1][1]+1) if stack else 2,6)
                stack.append((original_level,level))
                line='#'*level+' '+hm[2]+'\n'
            formatted.append(line)
        converted=''.join(formatted)
        scope='本文是 AlohaMini 项目资料，具体代际以原文路径和硬件配置为准。' if entry['category']=='alohamini' else '本文保留软件仓库的通用或进阶教程。示例中的机器人、数据集、路径和运行环境需按实际配置选择，不代表已经在 AlohaMini 2 / 2 Pro 上验证。'
        if 'pi0.5_openpi' in path: scope+=' 旧版部署接口与缺失启动脚本的说明见 [OpenPI 接入](../pi05.md)。'
        if kind=='hardware' and path=='AlohaMini1/docs/BOM.md': scope+=' 原文 Host/Client 说明前后有混用；本站统一称 Pi 为机器人端、PC 为操作端，供电需按实物额定值确认。'
        header=f'# {title}\n\n[← 教程资料库](../tutorial-library.md) · **{CATEGORIES[entry["category"]]} / 原文全文**\n\n{scope}\n\n来源：[{name} · `{path}`](https://github.com/{name}/blob/{rev}/{quote(path,safe="/")}) · 版本 `{rev[:8]}` · [下载未经改写的源文档]({rel(download)})\n\n本页保留原文语言及全部段落、表格和代码；仅调整标题层级、页面组件、代码围栏格式、相对链接和媒体路径。原文中的价格、性能和运行结果属于该版本记录。\n\n---\n\n'
        dest.write_text(localize_images(header+converted, dest))
    manifest={'date':'2026-09-28','sources':entries,'aliases':[{'kind':k[0],'path':k[1],'target':v,'page':pages[k]} for k,v in sorted(aliases.items())],'excluded':exclusions}
    (ROOT/'upstream-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    for key,label in CATEGORIES.items():
        rows=[e for e in entries if e['category']==key]
        page='# '+label+' · 原文资料\n\n以下页面已迁入本站，可在站内阅读和搜索。每篇保留固定版本来源与原始文件下载。\n\n[返回教程资料库](tutorial-library.md)\n\n```{toctree}\n:maxdepth: 1\n\n'
        for e in rows:
            label=e['title'].replace('<','').replace('>','').replace('\n',' ')
            page+=label+' <'+e['page'][:-3]+'>\n'
        (SOURCE/f'library-{key}.md').write_text(page+'```\n')
    print(f'Imported {len(entries)} full tutorials; resolved {len(aliases)} aliases; excluded {len(exclusions)} non-tutorial files.')
    print('Assets:',sum(len(e['assets']) for e in entries),'references;',sum(x['status']=='upstream-missing' for e in entries for x in e['assets']),'missing upstream references')

if __name__=='__main__': main()
