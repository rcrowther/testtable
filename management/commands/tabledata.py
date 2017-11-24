import collections

from testtable.models import BibleBooks, Country, Color, Tree, Mineral, Star

TableData = collections.namedtuple('TableData', 'model fields count filepath')


tabledata = {
'country' : TableData(Country, ['iso', 'name'], 254, './testtable/csv/countries.csv'), 
'color' : TableData(Color, ['name', 'title', 'hex', 'rgb'], 864, './testtable/csv/colors.csv'), 
'tree' : TableData(Tree, ['title', 'latin'], 419, './testtable/csv/trees.csv'), 
'biblebooks' : TableData(BibleBooks, ['james', 'vulgate', 'dv', 'auth'], 80, './testtable/csv/biblebooks.csv'), 
'mineral' : TableData(Mineral, ['name', 'isvalid', 'reason'], 1506, './testtable/csv/minerals.csv'), 
'star': TableData(Star, ['name', 'distance', 'magnitude', 'spectrum', 'color'], 87474,'./testtable/csv/stars.csv')
}

def to_string():
    b = ['Available dbs =\n']
    for key, table in tabledata.items():
        b.append("'")
        b.append(key)
        b.append("', entries:")
        b.append(str(table.count))
        b.append('\n')
    return ''.join(b)
        
