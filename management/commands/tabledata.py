import collections

from testdb.models import BibleBooks, Country, Color, Tree, Mineral, Star

TableData = collections.namedtuple('TableData', 'model fields count filepath')


tabledata = {
'country' : TableData(Country, ['iso', 'name'], 254, './testdb/csv/countries.csv'), 
'color' : TableData(Color, ['name', 'title', 'hex', 'rgb'], 864, './testdb/csv/colors.csv'), 
'tree' : TableData(Tree, ['title', 'latin'], 419, './testdb/csv/trees.csv'), 
'biblebooks' : TableData(BibleBooks, ['james', 'vulgate', 'dv', 'auth'], 80, './testdb/csv/biblebooks.csv'), 
'mineral' : TableData(Mineral, ['name', 'isvalid', 'reason'], 1506, './testdb/csv/minerals.csv'), 
'star': TableData(Star, ['name', 'distance', 'magnitude', 'spectrum', 'color'], 87474,'./testdb/csv/stars.csv')
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
        
