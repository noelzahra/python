"""
NLP isco coding with spaCy library
"""

import pandas as pd
from pathlib import Path

# Path(__file__).parent gives the directory where isco_coding.py lives, 
# so the file is found regardless of which directory you run the script from.

df = pd.read_excel(Path(__file__).parent / "ISCO_codes.xlsx", index_col=False)

codes_dict = df.set_index('Isco-08')['English title'].to_dict()

pd.DataFrame(list(codes_dict.items()), columns=["Isco-08", "English title"]).to_excel("ISCO_codes_dict.xlsx", index=False)

def main():
    print(len(df), "ISCO codes loaded.")
    print("ISCO codes:")
    for code, title in list(codes_dict.items())[:10]:
        print(f"  {code}: {title}")


if __name__ == "__main__":
    main()
