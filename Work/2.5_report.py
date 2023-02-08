# report.py
#
# Exercise 2.5

import csv,sys

def read_portfolio(filename):
    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for name,shares,price in rows:
            try:
                holding = {'name':name,'shares':int(shares),'price':float(price)}
                portfolio.append(holding)
            except ValueError:
                print("Couldn't parse", name, shares, price)
    return portfolio
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv'