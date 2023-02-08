# report.py
#
# Exercise 4.4
'''
Stuff and things go here
'''

import stock
from fileparse import parse_csv

def read_portfolio(filename:str) -> list:
    '''
    Read a stock portfolio into a list of dicts w/ keys name, shares, and price.
    '''
    portdicts = parse_csv(filename,select=['name','shares','price'],types=[str,int,float])
    portfolio = [stock.Stock(d['name'],d['shares'],d['price']) for d in portdicts]
    return portfolio

def read_prices(filename:str) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = parse_csv(filename,types=[str,float],has_headers=False)
    return dict(prices)
        
def holdings_change(portfolio:list,prices:dict) -> list:
    holdings = []
    for h in portfolio:
        current_price = prices[h.name]
        change = current_price - h.price
        summary = (h.name,h.shares,current_price,change)
        holdings.append(summary)
    return holdings

def print_report(table):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for n,s,p,c in table:
        p = '$' + str(f'{p:.2f}')
        print(f'{n:>10s} {s:>10d} {p:>10s} {c:>10.2f}')

def portfolio_report(portfolio_filename:str,prices_filename:str):
    # portfolio_file = input('Please provide the filepath for csv format portfolio data: ')
    # prices_file = input('Please provide the filepath for csv format ticker and price data: ')
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    earnings = holdings_change(portfolio,prices)
    print_report(earnings)

def main(argv):
    if len(argv) == 3:
        portfolio_file = argv[1]
        prices_file = argv[2]
    else:
        portfolio_file = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv'
        prices_file = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\prices.csv'
    
    portfolio_report(portfolio_file,prices_file)

if __name__ == '__main__':
    import sys
    main(sys.argv)