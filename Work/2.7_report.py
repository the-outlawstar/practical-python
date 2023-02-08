# report.py
#
# Exercise 2.7
'''
Tie all of this work together by adding a few additional statements to your report.py
program that computes gain/loss. These statements should take the list of stocks in
Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value
of the portfolio along with the gain/loss.
'''

import csv

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

def read_prices(filename):
    prices = {}
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        #next(rows)
        # originally tried iterating over two values, name,price but was not able to catch ValueError: not enough values to unpack (expected 2, got 0)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except (ValueError, IndexError):
                print(f"Couldn't parse {row} in {filename}")
        return prices

def current_portfolio_total(portfolio):
    total = 0
    for h in portfolio:
        total += h['shares'] * h['price']
    return total

def gain_loss(portfolio,prices):
    total = current_portfolio_total(portfolio)
    total_diff = 0
    loss_counter = 0
    gain_counter = 0
       
    for h in portfolio:
        if h['name'] in prices:
            if h['price'] < prices[h['name']]:
                gain_counter += 1
            else:
                loss_counter += 1
            total_diff += h['shares'] * prices[h['name']]
        else:
            total_diff += h['shares'] * h['price']
    if total < total_diff:
        print(f'Current portfolio value: ${total+total_diff:.02f}')
        print(f'Gain of: ${total_diff:.2f}')
    else:
        print(f'Current portfolio value: ${total-total_diff:.02f}')
        print(f'Loss of: ${total_diff:.2f}')