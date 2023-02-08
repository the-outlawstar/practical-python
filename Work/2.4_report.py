# report.py
#
# Exercise 2.4

import csv,sys

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                holding = (row[0],int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print("Couldn't parse", row)
    return portfolio
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv'