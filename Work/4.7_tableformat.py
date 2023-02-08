# tableformat.py

class TableFormatter:
    def headings(self,headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError

    def row(self,rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self,headers):
        for h in headers:
            print(f'{h:>10s}',end=' ')
        print()
        print(('-'*10+' ')*len(headers))

    def row(self,rowdata):
        for d in rowdata:
            print(f'{d:>10s}',end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in csv format.
    '''
    def headings(self,headers):
        print(','.join(headers))

    def row(self,rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self,headers):
        header = '<tr>'
        for h in headers:
            header += '<th>' + h + '</th>'
        header += '</tr>'
        print(header)

    def row(self,rowdata):
        r = '<tr>'
        for row in rowdata:
            r += '<td>' + row + '</td>'
        r += '</tr>'
        print(r)
        
def create_formatter(self,fmt:str='txt') -> TableFormatter:
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')