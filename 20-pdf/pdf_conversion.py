'''
    Pdf conersion to xls using camelot-py. Java needs to be installed in the system.
'''

import camelot
from pathlib import Path

tables = camelot.read_pdf(
    str(Path(__file__).parent / 'pdfs/99092086_Jan2026_ITB.pdf'),
    pages='all',
    password='osOcv5KA'
)

tables.export(
    str(Path(__file__).parent / '99092086_Jan2026_ITB.xlsx'),
    f='excel'
)

print(f"Exported {len(tables)} table(s) to 99092086_Jan2026_ITB.xlsx")
