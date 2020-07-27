import requests
from bs4 import BeautifulSoup

user_input = input('Hva ønsker du å se? vinn eller tap [default: vinn]: ')

if user_input == "tap":
    page = requests.get("https://www.nordnet.no/market/stocks?selectedTab=prices&sortField=diff_pct&sortOrder=asc&exchangeCountry=NO")
else:
    page = requests.get("https://www.nordnet.no/market/stocks?selectedTab=prices&sortField=diff_pct&sortOrder=desc&exchangeCountry=NO")

soup = BeautifulSoup(page.text, 'html.parser')



s = soup.find('a', class_='c02393 c02394').find_all(text=True, recursive=False)


names = soup.find_all('td', class_='c02380 c02383 c02387 c02381 borderBottom c02386 c02382')
values = soup.find_all(attrs={"class": "c02380 c02388 c02390 borderBottom c02373 c02386 c02382"})

max_c = 10
count = 0

print("***************************")

for name in names:          # Print all occurrences
    if count < max_c:
        print(str(name.get_text()) + " - " + str(values[count].get_text()))
        count = count + 1
    else:
        print("***************************")
        exit()

