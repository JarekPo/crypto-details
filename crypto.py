from locale import currency
from urllib import request
import requests

coinsList = None
currency = 'EUR'

def getCryptoInfo():
    # [ {'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}} ]
    global coinsList
    response = requests.get('https://api.coingecko.com/api/v3/coins/list?include_platform=true')
    if response.ok == True:
        data = response.json()
        print('Server OK')
        print('Number of coins: ',str(len(data)))
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
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+coinId+'&vs_currencies='+currency+'&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true')
    if response.ok:
        print('Server OK')
        data = response.json()
        return data
    else:
        return None
foundCoin = findCoinBySymbol('btc')
print(foundCoin)
marketData = getCoinMarketData(foundCoin['id'])
print('Market data: ',marketData)