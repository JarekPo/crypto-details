
from os import system
from time import sleep
import requests

coinsList = None
currency = 'EUR'

def clear():
    _ = system('cls')

def getCryptoInfo():
    # [ {'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}} ]
    global coinsList
    response = requests.get('https://api.coingecko.com/api/v3/coins/list?include_platform=true')
    if response.ok == True:
        data = response.json()
        coinsList = data
getCryptoInfo()

def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin['symbol'] == symbol:
            return coin
    else:
        return None

def getCoinMarketData(coinId):
    # {'bitcoin': {'eur': 19837.61, 'eur_market_cap': 380189281070.3365, 'eur_24h_vol': 35788343727.42923, 'eur_24h_change': -1.7484662702426028, 'last_updated_at': 1664515472}}
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+coinId+'&vs_currencies='+currency+'&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true')
    if response.ok:
        data = response.json()
        return data
    else:
        return None

def getCoinsPrice(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinMarketData(coinId)
    return marketData[coinId][currency]

clear()
print('\nWelcome to the crypto currency exchange calculator service')
sleep(1)
currency = input('\nEnter your local currency symbol (eg. USD): ').upper()

while True:
    currencyToBuy = input('\nEnter the required crypto currency symbol or presseur "Q" to exit: ')
    if currencyToBuy.lower() == 'q':
        break
    
    requiredCoin = findCoinBySymbol(currencyToBuy)
    if requiredCoin == None:
        sleep(1)
        clear()
        print('Currency not found')
        continue

    requiredCoinPrice = getCoinsPrice(requiredCoin['id'], currency)
    sleep(1)
    clear()
    print('Your currency:', currency)
    print('Crypto currency:', requiredCoin['name'])
    print('1', requiredCoin['name'], '=', requiredCoinPrice, currency)
    userBudget = float(input('How much money do you want to spend? '))
    userBudgetToCoins = round(userBudget/requiredCoinPrice, 2)
    sleep(1)
    print('\nFor','\033[92m',userBudget,currency,'\033[0m','you can buy','\033[92m',userBudgetToCoins,currencyToBuy,'\033[0m')