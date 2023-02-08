# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename:str) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if not select==None:
                indices = [ headers.index(colname) for colname in select ]
                record = { colname: row[index] for colname, index in zip(select, indices) }
                records.append(record)
            else:
                record = dict(zip(headers, row))
                records.append(record)

    return records