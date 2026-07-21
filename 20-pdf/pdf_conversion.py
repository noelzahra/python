'''
    Pdf conersion to xls using camelot-py. Java needs to be installed in the system.
'''

import camelot
import pandas as pd
from pathlib import Path

tables = camelot.read_pdf(
    str(Path(__file__).parent / 'pdfs/99092086_Jan2026_ITB.pdf'),
    pages='all',
    password='osOcv5KA'
)

output_file = tables.export (
    str(Path(__file__).parent / 'pdfs/99092086_Jan2026_ITB.csv'),
    f='csv'
)

df = pd.read_csv(str(Path(__file__).parent / '99092086_Jan2026_ITB.csv'), encoding='utf-8', dtype=str)
print(df.head())
