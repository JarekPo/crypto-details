
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
    # {'bitcoin': {'eur': 19837.61, 'eur_market_cap': 380189281070.3365, 'eur_24h_vol': 35788343727.42923, 'eur_24h_change': -1.7484662702426028, 'last_updated_at': 1664515472}}
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+coinId+'&vs_currencies='+currency+'&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true')
    if response.ok:
        print('Server OK')
        data = response.json()
        return data
    else:
        return None

def getCoinsPrice(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinMarketData(coinId)
    return marketData[coinId][currency]


foundCoin = findCoinBySymbol('btc')
print(foundCoin)

marketData = getCoinMarketData(foundCoin['id'])
print('Market data: ',marketData)

coinPrice = getCoinsPrice(foundCoin['id'], currency)
print(foundCoin['id'],'price: ',coinPrice, currency)


