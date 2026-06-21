"""
NLP isco coding with spaCy library
"""

import pandas as pd
from pathlib import Path

df = pd.read_excel(Path(__file__).parent / "Over70-all-interviewers-distribution.xlsx", index_col=False)

def get_interviewer(df): 
    each_interviewer = df['User'].unique()
    for interviewer in each_interviewer:
        print(f"Hello {interviewer} from spaCy!")


def main():
    get_interviewer(df)


if __name__ == "__main__":
    main()
