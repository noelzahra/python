from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.scrapethissite.com/pages/forms/'
response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find_all('tr', class_='team')

teams = {}
for row in rows:
    name = row.find('td', class_='name').text.strip()
    year = row.find('td', class_='year').text.strip()
    wins = row.find('td', class_='wins').text.strip()
    losses = row.find('td', class_='losses').text.strip()
    ot_losses = row.find('td', class_='ot-losses').text.strip()
    win_pct = row.find('td', class_='pct').text.strip()
    gf = row.find('td', class_='gf').text.strip()
    ga = row.find('td', class_='ga').text.strip()
    diff = row.find('td', class_='diff').text.strip()

    entry = {
        'year': year,
        'wins': wins,
        'losses': losses,
        'ot_losses': ot_losses,
        'win_pct': win_pct,
        'goals_for': gf,
        'goals_against': ga,
        'diff': diff,
    }

    if name not in teams:
        teams[name] = []
    teams[name].append(entry)

print(json.dumps({'Boston Bruins': teams.get('Boston Bruins')}, indent=2))
