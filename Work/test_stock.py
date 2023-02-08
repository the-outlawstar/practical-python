# test_stock.py

import unittest,stock

class TestStock(unittest.TestCase):
    
    def test_create(self):
        s = stock.Stock('GOOG',100,490.1)
        self.assertEqual(s.name,'GOOG')
        self.assertEqual(s.shares,100)
        self.assertEqual(s.price,490.1)
        
    def test_cost(self):
        s = stock.Stock('GOOG',100,490.1)
        self.assertEqual(s.cost,(100*490.1))

    def test_sell(self):
        s = stock.Stock('GOOG',100,490.1)
        self.assertEqual(s.sell(25),(100-25))

    def test_bad_shares(self):
        s = stock.Stock('GOOG',100,490.1)
        with self.assertRaises(TypeError):
            s.shares = '100'


if __name__ == '__main__':
    # Use this when running interactively
    #unittest.main(exit=False)
    unittest.main()