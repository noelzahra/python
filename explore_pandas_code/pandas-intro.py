# Pandas

import pandas as pd
import requests

print(pd.__version__)

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/nba-elo/nbaallelo.csv"
response = requests.get(download_url)
print(response.status_code)

with open('nba_all_elo.csv', 'wb') as f:
    f.write(response.content)

dir

nba= pd.read_csv('nba_all_elo.csv')
type(nba)

len(nba)
