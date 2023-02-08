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

def read_portfolio(filename):
    with open(filename,'rt') as f:
        # this does not convert types
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        indices = [ headers.index(colname) for colname in select ]
        portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
    return portfolio

def read_prices(filename):
    # Tried using dict comprehension, couldnt figure it out...
    prices = {}
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        # originally tried iterating over two values, name,price but was not able to catch ValueError: not enough values to unpack (expected 2, got 0)
        # try:
        #     prices = {row[0]: float(row[1]) for row in rows}
        #     #return prices
        # except (ValueError, IndexError):
        #     print(f"Row: n Couldn't parse row in {filename}")
        for n,row in enumerate(rows,start=1):
            try:
                prices[row[0]] = float(row[1])
            except (ValueError, IndexError):
                print(f"Row: {n} Couldn't parse {row} in {filename}")
    return prices
        

def current_portfolio_total(portfolio):
    # Multiplies the shares by their prices, then sums all values
    return sum([h['shares'] * h['price'] for h in portfolio])

def gain_loss(portfolio,prices):
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
        #total_diff += h['shares'] * prices[h['name']]
    if total < total_diff:
        print(f'Current portfolio value: ${total+total_diff:.02f}')
        print(f'Gain of: ${total_diff:.2f}')
    else:
        print(f'Current portfolio value: ${total-total_diff:.02f}')
        print(f'Loss of: ${total_diff:.2f}')
    return holding_gain_loss

def make_report(table):
    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = '---------- ---------- ---------- ----------'
    print('%10s %10s %10s %10s' % headers)
    print('%10s' % separator)
    #for r in table:
    for n,s,p,c in table:
        #print('%10s %10d %10.2f %10.2f' % r)
        p = '$' + str(f'{p:.2f}')
        #print(p)
        print(f'{n:>10s} {s:>10d} {p:>10s} {c:>10.2f}')