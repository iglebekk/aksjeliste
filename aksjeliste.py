import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os


def clean_up(var):
    location = var.find("%")+1
    var = var[1:location]
    return(var)



def get_data(page, sign):
    soup = BeautifulSoup(page.text, 'html.parser')
    s = soup.find('a', class_='c02393 c02394').find_all(text=True, recursive=False)
    names = soup.find_all('td', class_='c02380 c02383 c02387 c02381 borderBottom c02386 c02382')
    values = soup.find_all(attrs={"class": "c02380 c02388 c02390 borderBottom c02373 c02386 c02382"})
    max_c = 20  
    count = 0
    
    rows = list()
    for name in names:          # Print all occurrences
        if count < max_c:
            value = sign + clean_up(values[count].get_text())
            rows.append([str(name.get_text()), clean_up(str(value))])
            count = count + 1

    print(
        tabulate(
                rows, 
                headers=['Stock', '%'], 
                tablefmt='orgtbl'
                )
        )

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('')
        print("******************************VINNERE******************************")
        page = requests.get("https://www.nordnet.no/market/stocks?selectedTab=prices&sortField=diff_pct&sortOrder=desc&exchangeCountry=NO")
        get_data(page, "+")
        print('')
        print("******************************TAPERE******************************")
        page = requests.get("https://www.nordnet.no/market/stocks?selectedTab=prices&sortField=diff_pct&sortOrder=asc&exchangeCountry=NO")
        get_data(page, "-")
        print('')
        print('')
        ui = input("Press Enter to refresh or 'q' to quit: ")
        if(ui == 'q'):
            print('')
            exit('Exiting... \n')