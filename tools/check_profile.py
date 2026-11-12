from pathlib import Path
import re
p=Path(__file__).resolve().parents[1]
files=['README.md','README.zh-CN.md','README.zh-TW.md','README.ja.md','README.ko.md']
order=['open-game-skills','MagMark','ComfyUI_PaintingCoderUtils','github-risers','reverse-engineering-atlas','awesome-ai-model-showcases']
for name in files:
 s=(p/name).read_text()
 assert len(re.findall(r'^# ',s,re.M))==1,name
 assert '<table' not in s and 'min-width' not in s,name
 assert [r for r in order if f'https://github.com/jammyfu/{r}' in s]==order
 assert sorted(order,key=lambda r:s.index('https://github.com/jammyfu/'+r))==order
 for f in files:assert f in s,(name,f)
 for src in re.findall(r'src="([^"]+)"',s):assert (p/src).is_file(),src
 for url in re.findall(r'https://[^\s)"<>]+',s):assert url.startswith('https://github.com/jammyfu'),url
 assert s.count('<img ')==3,name
 assert 'awesome-gpt-image-gifs' not in s
 print('PASS',name)
print('PASS: five languages, project order, media, owned links, one H1, no layout tables')
