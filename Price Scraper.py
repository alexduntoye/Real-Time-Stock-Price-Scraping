import bs4

import requests

import time
try:
    quote = input("Enter a stock quote symbol:\n")


except:
    print('please enter a yahoo quote symbol')


def parsePrice():
    r = requests.get('https://uk.finance.yahoo.com/quote/' + str(quote) + '?p=' + str(quote))
    soup = bs4.BeautifulSoup(r.text, "html.parser")

    price = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text

    return price


while True:
    print('the current price: ' + str(parsePrice()))
    time.sleep(40)

