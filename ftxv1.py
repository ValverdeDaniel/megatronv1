import ccxt
#ftx api key and secret
apiKey = 'G81GdgkuuKSEirOzjEWtzHrtwA80185s4UVCVNBj'
apiSecret = 'rFVklFWKa-UypGmnG61Jl4YzT4zkCW733DLA8JN5'
ftx = ccxt.ftxus()
markets = ftx.load_markets()
# print(binance.id, markets)
# orderbookBTC = ftx.fetchOrderBooks('BTC/USDT', limit = 20)
# print(orderbookBTC)
ethusd = ftx.markets['ETH/USD']
print(ethusd)
