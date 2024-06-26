import json
import random
import urllib.request

prices = {}

QUERY = "http://localhost:8080/query?id={}"

N = 300


def getdatapoint(quote):
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price


def getratio(price_a, price_b):
    if price_b == 0:
        return
    return price_a/price_b


if __name__ == "__main__":

    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getdatapoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        print("Ratio %s" % getratio(prices["ABC"], prices["DEF"]))
