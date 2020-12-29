from yahoo_fin import stock_info
import alpaca_trade_api
import yfinance
import KEYS
from time import sleep
from datetime import datetime
import time
yfinance.pdr_override()
API_KEY = "PK90FW93OCL2BSYMYQJS"
API_SECRET = "tYayl4E8FoJ4uscqrKmT7EmCvbPwR0142hxHTHTW"
BASE_URL = "https://paper-api.alpaca.markets"
apithing = alpaca_trade_api.REST(API_KEY, API_SECRET, BASE_URL)
def get_price(ticker: str):
    try:
        return stock_info.get_live_price(ticker)
    except AssertionError:
        return
Stock = ["XOM","CVX","SLB","COP","FB","GOOGL","ATVI","NFLX","AAPL","MSFT","V","NVDA","BRK.B","JPM","BAC","C"]
Amount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Buyprice = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
open = 7
totalstock = 16
done = False
close = 13
totalmoney = 400000
stocksleft = 16
while (done == False):
    now = datetime.now()
    if (close > now.hour and open < now.hour):
        for i in range(totalstock):
            money = totalmoney//stocksleft
            numberofshares = money//(get_price(Stock[i]))
            Amount[i] = numberofshares
            Buyprice[i] = get_price(Stock[i])
            totalmoney -= Amount[i] * Buyprice[i]
            stocksleft -= 1
            apithing.submit_order(Stock[i], numberofshares,'buy', 'market', 'day')
            print("Buying " + numberofshares + " of " + Stock[i])
        done = True
    else:
        time.sleep(60)
if (done):
    print(Amount)
    print(Buyprice)
