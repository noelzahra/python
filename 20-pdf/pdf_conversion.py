'''
    Pdf conersion to xls using camelot-py. Java needs to be installed in the system.
'''

import re

import camelot
import pandas as pd
from pathlib import Path

ILLEGAL_CHARACTERS_RE = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]')

tables = camelot.read_pdf(
    str(Path(__file__).parent / 'Invoice-ACC2026-0214.pdf'),
    pages='all',
    flavor='stream'
)

if not tables:
    raise ValueError("No tables found in PDF")

for table in tables:
    table.df = table.df.map(
        lambda v: ILLEGAL_CHARACTERS_RE.sub('', v) if isinstance(v, str) else v
    )

tables.export(
    str(Path(__file__).parent / 'Invoice-ACC2026-0214.xlsx'),
    f='excel'
)

# print(f"Exported {len(tables)} table(s) to 99092086_Jan2026_ITB.xlsx")


df = pd.read_excel(Path(__file__).parent / "Invoice-ACC2026-0214.xlsx", index_col=False)
print(df.head())
df.to_excel('Invoice-ACC2026-0214 final.xlsx', index =False)
print('Call history xls file saved')

