# pcost.py
#
# Exercise 3.13
import sys
from report import read_portfolio

def portfolio_cost(filename):
    records = read_portfolio(filename)
    return sum([h.cost for h in records])

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv'
    cost = portfolio_cost(filename)
    print(f'Total cost: ${cost}')

if __name__ == '__main__':
    import sys
    main(sys.argv)