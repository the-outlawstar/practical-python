# report.py
#
# Exercise 2.16
'''
Tie all of this work together by adding a few additional statements to your report.py
program that computes gain/loss. These statements should take the list of stocks in
Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value
of the portfolio along with the gain/loss.
'''

import csv

def read_portfolio(filename:str) -> list:
    '''
    Read a stock portfolio into a list of dicts w/ keys name, shares, and price.
    '''
    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n,row in enumerate(rows):
            try:
                holding = dict(zip(headers,row))
                stock = {'name':holding['name'],'shares':int(holding['shares']),
                        'price':float(holding['price'])}
                portfolio.append(stock)
            except(ValueError, IndexError):
                print(f"Row: {n} Couldn't parse {row} in {filename}")
    return portfolio

def read_prices(filename:str) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    # Dict comp requires using try/except as a func....
    prices = {}
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        for n,row in enumerate(rows,start=1):
            try:
                prices[row[0]] = float(row[1])
            except(ValueError, IndexError):
                print(f"Row: {n} Couldn't parse {row} in {filename}")
    return prices
        

def current_portfolio_total(portfolio:list) -> float:
    '''
    Expects input from read_portfolio() output. Multiplies the shares by their prices, 
    then sums all values
    '''
    return sum([h['shares'] * h['price'] for h in portfolio])

def gain_loss(portfolio:list,prices:dict) -> list:
    # Seems quite large?, make gain func, loss func?
    total = current_portfolio_total(portfolio)
    total_diff = 0
    holding_gain_loss = []

    loss = sum([prices[h['name']]-h['price'] for h in portfolio if h['price'] > prices[h['name']]])
    gain = sum([prices[h['name']]-h['price'] for h in portfolio if h['price'] < prices[h['name']]])
       
    for h in portfolio:
        if h['name'] not in prices:
            total_diff += h['shares'] * h['price']
        elif h['price'] < prices[h['name']]:
            gain = prices[h['name']] - h['price']
            holding_gain_loss.append((h['name'],h['shares'],prices[h['name']],gain))
            total_diff += h['shares'] * prices[h['name']]
        elif h['price'] > prices[h['name']]:
            loss = prices[h['name']]-h['price']
            holding_gain_loss.append((h['name'],h['shares'],prices[h['name']],loss))
            total_diff += h['shares'] * prices[h['name']]
    if total < total_diff:
        print(f'Current portfolio value: ${total+total_diff:.02f}')
        print(f'Gain of: ${total_diff:.2f}')
    else:
        print(f'Current portfolio value: ${total-total_diff:.02f}')
        print(f'Loss of: ${total_diff:.2f}')
    return holding_gain_loss

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
    earnings = gain_loss(portfolio,prices)
    print_report(earnings)