# Exercise 2.15
import csv,sys
def portfolio_cost(filename):
    total_cost = 0
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for n,row in enumerate(rows,start=1):
            record = dict(zip(header,row))
            try:
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f"Row: {n} Couldn't parse {row}")
    return total_cost
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')