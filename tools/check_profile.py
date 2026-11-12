from pathlib import Path
from urllib.parse import urlparse
import re,json
p=Path(__file__).resolve().parents[1]
files=['README.md','README.zh-CN.md','README.zh-TW.md','README.ja.md','README.ko.md']
expected=['open-game-skills','TheLegendOfTrump','MagMark','xiangsheng-genealogy','ComfyUI_PaintingCoderUtils']
for name in files:
 s=(p/name).read_text()
 assert len(re.findall(r'^# ',s,re.M))==1,name
 assert sorted(expected,key=lambda r:s.index('https://github.com/jammyfu/'+r))==expected
 for f in files: assert f in s,(name,f)
 for src in re.findall(r'src="([^"]+)"',s):
  if not src.startswith('https://'):assert (p/src).is_file(),src
  else:assert src.startswith('https://raw.githubusercontent.com/jammyfu/'),src
 for url in re.findall(r'https://[^\s)"<>]+',s):
  u=urlparse(url);assert u.netloc in ['github.com','raw.githubusercontent.com'],url
  assert u.path.split('/')[1]=='jammyfu',url
 assert s.count('<img ')==6 and s.count('width="140"')==5 and s.count('width="84"')==1,name
 assert '<details>' not in s and '<summary>' not in s, name
 assert len([line for line in s.splitlines() if line.startswith('| **[')]) == 5, name
 assert ' |<br>' not in s, name
 assert 'awesome-gpt-image-gifs' not in s
 assert s.count('https://github.com/jammyfu?tab=repositories') == 1, name
 assert s.count('| --- | --- |') == 1, name
 assert '#selected-work' not in s and '#public-projects' not in s, name
 print('PASS',name)
print('PASS: 5 featured projects + one full project-list link, five languages, compact original-media preview tables, owner-only URLs, files and compact layout')
