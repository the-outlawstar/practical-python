import csv,sys
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
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'C:\\Users\\NTM\\Documents\\Neil\\python\\practical-python\\Work\\Data\\prices.csv'