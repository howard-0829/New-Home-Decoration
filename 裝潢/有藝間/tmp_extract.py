from pathlib import Path
from pypdf import PdfReader
pdf = Path(r'C:\Users\showard308\Desktop\預售屋議價\裝潢\有藝間\有藝間創意室內設計 - 工程報價單（羅浮b6-23F）（修改）.pdf')
print('exists', pdf.exists(), 'size', pdf.stat().st_size if pdf.exists() else 0)
r = PdfReader(str(pdf))
print('pages', len(r.pages))
for i, page in enumerate(r.pages[:10], 1):
    text = page.extract_text() or ''
    print(f'---PAGE {i} START---')
    print(text[:3000])
    print(f'---PAGE {i} END---')
