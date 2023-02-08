# pcost.py
#
# Exercise 1.30
def portfolio_cost(filename):
    total_cost = 0
    with open(filename,'rt') as f:
        next(f)
        for line in f:
            row = line.strip().split(',')
            total_cost += int(row[1]) * float(row[2])
    return total_cost

cost = portfolio_cost('C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv')
print(f'Total cost: {cost}')