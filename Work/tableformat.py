'''
Created on 18.02.2022

@author: ho_ksk
__updated__='2022-02-18 11:48:57'
'''

class TableFormatter():
    '''
    classdocs
    '''
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()
        
        
    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()
        
        

class TextTableFormatter(TableFormatter):
    
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10  + ' ') * len(headers))
        
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10}', end=' ')
        print()
        
        
class CSVTableFormatter(TableFormatter):
    
    def headings(self, headers):
        print(','.join(headers))
        
    def row(self, rowdata):
        print(','.join([str(d) for d in rowdata]))
        
        
class HTMLTableFormatter(TableFormatter):
    
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<td>{h}</td>', end='')
        print('</tr>')
        
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
        
        
        
        
def create_formatter(name):        
    if name == 'txt':
        return TextTableFormatter()
    if name == 'csv':
        return CSVTableFormatter()
    if name == 'html':
        return HTMLTableFormatter()
        
        
        
        
        
        
        
        
        
        
        
        