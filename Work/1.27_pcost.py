# pcost.py
#
# Exercise 1.27
total_cost = 0
f = open('C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\portfolio.csv','rt')
next(f)
for line in f:
  row = line.strip().split(',')
  total_cost += int(row[1]) * float(row[2])
print(f'Total cost {total_cost}')
f.close()