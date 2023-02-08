# report.py
#
# Exercise 4.4
'''
Stuff and things go here
'''

import stock,tableformat
from portfolio import Portfolio
from fileparse import parse_csv

def read_portfolio(filename:str) -> list:
    '''
    Read a stock portfolio into a list of dicts w/ keys name, shares, and price.
    '''
    portdicts = parse_csv(filename,select=['name','shares','price'],types=[str,int,float])
    portfolio = [stock.Stock(**d) for d in portdicts]
    return Portfolio(portfolio)

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

def print_report(reportdata,formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for n,s,p,c in reportdata:
        # p = '$' + str(f'{p:.2f}')
        # print(f'{n:>10s} {s:>10d} {p:>10s} {c:>10.2f}')
        rowdata = [n, str(s), f'{p:0.2f}', f'{c:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename:str,prices_filename:str,fmt='txt'):
    # portfolio_file = input('Please provide the filepath for csv format portfolio data: ')
    # prices_file = input('Please provide the filepath for csv format ticker and price data: ')
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    earnings = holdings_change(portfolio,prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(earnings,formatter)

def main(argv):
    if len(argv) == 4:
        portfolio_file = argv[1]
        prices_file = argv[2]
        format = argv[3]
        return portfolio_report(portfolio_file,prices_file,format)
    elif len(argv) == 3:
        portfolio_file = argv[1]
        prices_file = argv[2]
        return portfolio_report(portfolio_file,prices_file)
    else:
        portfolio_file = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv'
        prices_file = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\prices.csv'
        return portfolio_report(portfolio_file,prices_file)

if __name__ == '__main__':
    import sys
    main(sys.argv)