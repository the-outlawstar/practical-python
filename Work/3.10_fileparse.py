# fileparse.py
#
# Exercise 3.10
import csv

def parse_csv(filename:str,select:list=[],types:list=[],has_headers:bool=True,delimiter:str=',',silence_errors:bool=False) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f,delimiter=delimiter)
        if select and not has_headers and not silence_errors:
            raise RuntimeError("select argument requires column headers")
        if has_headers:
            headers = next(rows)
        records = []
        # If a column selector was given, find indicies of the specified columns
        # Also narrow the set of headers used for resulting dicts.
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select
        else:
            indices = []
        for n,row in enumerate(rows,start=1):
            if not row:    # Skip rows with no data
                continue
            if indices:    # Filter the row if specific columns were selected
                row = [row[index] for index in indices]
            if types:    # Convert row values if types were provided
                try:
                    row = [func(val) for func, val in zip(types,row)]
                except(ValueError) as e:
                    if not silence_errors:
                        print(f"Row: {n} Couldn't convert {row} in {filename}, Reason: {e}")
            if not has_headers:
                record = tuple(row)
            else:
                record = dict(zip(headers, row))
            records.append(record)

    return records