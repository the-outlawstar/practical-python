# pcost.py
#
# Exercise 3.13
import csv,sys
from report import read_portfolio

def portfolio_cost(filename):
    records = read_portfolio(filename)
    return sum([h['shares'] * h['price'] for h in records])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')