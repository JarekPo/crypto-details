import requests

coinsList = None

def getCryptoInfo():
    # [ {'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}} ]
    global coinsList
    response = requests.get('https://api.coingecko.com/api/v3/coins/list?include_platform=true')
    if response.ok == True:
        data = response.json()
        print('Server OK')
        print(data[0])
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

foundCoin = findCoinBySymbol('eth')
print(foundCoin)

