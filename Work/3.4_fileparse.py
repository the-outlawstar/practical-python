# fileparse.py
#
# Exercise 3.4
import csv

def parse_csv(filename:str,select:list=[]) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select
        else:
            indices = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if indices:
                row = [row[index] for index in indices]
        
            record = dict(zip(headers, row))
            records.append(record)

    return records