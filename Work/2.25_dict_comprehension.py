import csv

def read_dow_stocks(filename):
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        types = [str, float, str, str, float, float, float, float, int]
        #select = ['name', 'shares', 'price']
        #indices = [ headers.index(colname) for colname in select ]
        #portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
        portfolio = [{name:func(val) for name,func,val in zip(headers,types,row)} for row in rows]
        for h in portfolio:
            h['date'] = tuple([int(i) for i in h['date'].split('/')])
    return portfolio    
    pass