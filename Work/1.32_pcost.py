# pcost.py
#
# Exercise 1.32
def portfolio_cost(filename):
    import csv
    total_cost = 0
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", row)
    return total_cost

cost = portfolio_cost('C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv')
print(f'Total cost: {cost}')