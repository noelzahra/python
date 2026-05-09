from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

team = soup.find('td', class_='name').text.strip()
print(team)

'''teams = sorted(soup.find_all('td', class_='name'), key=lambda x: x.text.strip())
for team in teams:
    print(team.text.strip())
'''
wins = sorted(soup.find_all('td', class_='wins'), key=lambda x: x.text.strip())
list_of_wins = []
for win in wins:
    list_of_wins.append(win.text.strip())
print(list_of_wins)