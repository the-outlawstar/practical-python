# ticker.py

from .follow import follow
import csv,report,tableformat

def select_columns(rows,indices):
    # for row in rows:
    #     yield [row[index] for index in indices]
    return ([row[index] for index in indices] for row in rows)

def convert_types(rows,types):
    # for row in rows:
    #     yield [func(val) for func,val in zip(types,row)]
    return ([func(val) for func,val in zip(types,row)] for row in rows)

def make_dicts(rows,headers):
    # for row in rows:
    #     yield dict(zip(headers,row))
    return (dict(zip(headers,row)) for row in rows)

def filter_symbols(rows,names):
    # for row in rows:
    #     if row['name'] in names:
    #         yield row
    return (row for row in rows if row['name'] in names)
    #pass

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows,[0,1,4])
    rows = convert_types(rows,[str,float,float])
    rows = make_dicts(rows,['name','price','change'])
    return rows

def ticker(portfile,logfile,fmt):
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    portfolio = report.read_portfolio(portfile)
    rows = filter_symbols(rows,portfolio)
    #rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([row['name'],f"{row['price']:.2f}",f"{row['change']:.2f}"])

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile logfile fmt' % args[0])
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)