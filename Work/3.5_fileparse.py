# fileparse.py
#
# Exercise 3.5

import csv

def parse_csv(filename:str,select:list=[],types:list=[]) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        # If a column selector was given, find indicies of the specified columns
        # Also narrow the set of headers used for resulting dicts.
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select
        else:
            indices = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if indices:    # Filter the row if specific columns were selected
                row = [row[index] for index in indices]
            if types:    # Convert row values if types were provided
                row = [func(val) for func, val in zip(types,row)]
            else:
                record = dict(zip(headers, row))
            records.append(record)

    return records