import unittest
from client3 import getdatapoint, getratio


class ClientTest(unittest.TestCase):
    def test_getdatapoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getdatapoint(quote), (quote['stock'], quote['top_bid']['price'],
                                                   quote['top_ask']['price'], (quote['top_bid']['price']
                                                                               + quote['top_ask']['price']) / 2))

    def test_getdatapoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getdatapoint(quote), (quote['stock'], quote['top_bid']['price'],
                                                   quote['top_ask']['price'], (quote['top_bid']['price']
                                                                               + quote['top_ask']['price']) / 2))

    def test_getratio_priceBZero(self):
        price_a = 119.2
        price_b = 0
        self.assertIsNone(getratio(price_a, price_b))




if __name__ == '__main__':
    unittest.main()
