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
from fileparse import parse_csv

def read_portfolio(filename:str) -> list:
    '''
    Read a stock portfolio into a list of dicts w/ keys name, shares, and price.
    '''
    portfolio = parse_csv(filename,select=['name','shares','price'],types=[str,int,float])
    return portfolio

def read_prices(filename:str) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = parse_csv(filename,types=[str,float],has_headers=False)
    return dict(prices)
        

def current_portfolio_total(portfolio:list) -> float:
    '''
    Expects input from read_portfolio() output. Multiplies the shares by their prices, 
    then sums all values
    '''
    return sum([h['shares'] * h['price'] for h in portfolio])

def portfolio_gain(portfolio:list,prices:list) -> tuple:
    total_gain = 0
    holding_gain = []
    for h in prices:
        print(h)
        if h[0] not in portfolio['name']:
            continue
        elif portfolio['price'] < h[1]:
            gain = h[1] - portfolio['price']
            total_gain += gain
            holding_gain.append((portfolio['name'],portfolio['shares'],h[1],gain))
    return total_gain,holding_gain

def portfolio_loss(portfolio:list,prices:list) -> tuple:
    total_loss = 0
    holding_loss = []
    for n,h in enumerate(portfolio):
        if h['name'] not in prices[n]:
            continue
        elif h['price'] > prices[n][1]:
            loss = prices[n][1] - h['price']
            total_loss += loss
            holding_loss.append((h['name'],h['shares'],prices[n][1],loss))
    return total_loss,holding_loss

def gain_loss(portfolio:list,prices:dict) -> list:
    # Seems quite large?, make gain func, loss func?
    total = current_portfolio_total(portfolio)
    total_diff = 0
    holding_gain_loss = []

    #loss = sum([prices[h['name']]-h['price'] for h in portfolio if h['price'] > prices[h['name']]])
    #gain = sum([prices[h['name']]-h['price'] for h in portfolio if h['price'] < prices[h['name']]])
           
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