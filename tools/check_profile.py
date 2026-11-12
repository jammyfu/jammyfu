from pathlib import Path
from urllib.parse import urlparse
import re,json
p=Path(__file__).resolve().parents[1]
files=['README.md','README.zh-CN.md','README.zh-TW.md','README.ja.md','README.ko.md']
expected=['open-game-skills','TheLegendOfTrump','MagMark','xiangsheng-genealogy','ComfyUI_PaintingCoderUtils','github-risers','reverse-engineering-atlas','awesome-ai-model-showcases','TokenSpeedSimulator','bitmap-vector-studio','local-tool-skill','llm_gpu_toolkit','hf-download-list','MiiAIPlaza','photo-spec-library','awesome-game-assets','practical-oss']
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
 assert s.count('<img ')==6 and s.count('width="880"')==5 and s.count('width="640"')==1,name
 assert 'awesome-gpt-image-gifs' not in s
 assert 'id="selected-work"' in s and 'id="public-projects"' in s
 print('PASS',name)
print('PASS: 17 public projects, five languages, large original-media previews, owner-only URLs, anchors and files')
