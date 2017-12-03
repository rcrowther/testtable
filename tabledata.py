import collections

from testtable.models import (
ChristmasSong, BibleBooks, Country, Color, Tree, Mineral, Star
)

TableData = collections.namedtuple('TableData', 'model description fields count filepath')


tabledata = {
'12days' : TableData(
    ChristmasSong, "Twelve days of Christmas song.",
    ['gift'], 12, './testtable/csv/twelvedaysofchristmas.csv'
),
'country' : TableData(
    Country, "Country name and 2-codepoint ISO codes.",
    ['iso', 'name'], 254, './testtable/csv/countries.csv'
), 
'color' : TableData(
    Color, "HTML color names and hex/rgb values",
    ['name', 'title', 'hex', 'rgb'], 864, './testtable/csv/colors.csv'
), 
'tree' : TableData(
    Tree, "A few English trees and their Latin names",
    ['title', 'latin'], 419, './testtable/csv/trees.csv'
), 
'biblebooks' : TableData(
    BibleBooks, "Books from the King James Bible with references to other notable Bibles",
    ['james', 'vulgate', 'dv', 'auth'], 80, './testtable/csv/biblebooks.csv'
), 
'mineral' : TableData(
    Mineral, "List of common mineral names, true/false if the mineral is scientificly classified, and why",
    ['name', 'isvalid', 'reason'], 1506, './testtable/csv/minerals.csv'
), 
'star': TableData(
    Star, "Data on visible stars with common name, distance, magnitude, and color data", 
    ['name', 'distance', 'magnitude', 'spectrum', 'color'], 87474, './testtable/csv/stars.csv'
)
}

def exists(name):
    data = tabledata[name]
    return (data.model.objects.count() > 0)

#.OperationalErro
def exists_lists():
    exists = []
    available = []
    for name, data in tabledata.items():
      if (data.model.objects.count() > 0):
          exists.append(name)
      else:
          available.append(name)
    return (exists, available)

def extendto(size, b):
    l = 0
    for s in b:
      l += len(s)
    if l < size:
      b.append(' ' *(size - l))
    
def to_string():
    e, a = exists_lists()
    b = []
    b.append('Installed tables:\n')
    for key in e:
        bb = []
        bb.append("  ")
        bb.append(key)
        extendto(16, bb)
        bb.append("size:")
        bb.append(str(tabledata[key].count))
        bb.append('\n')    
        b.extend(bb)
    b.append('Available tables:')
    for key in a:
        bb = []
        bb.append("  ")
        bb.append(key)
        extendto(16, bb)
        bb.append("size:")
        bb.append(str(tabledata[key].count))
        extendto(28, bb)
        bb.append("cols:")
        bb.append(str(len(tabledata[key].fields)))
        extendto(36, bb)
        bb.append(tabledata[key].description)
        b.append('\n')
        b.extend(bb)  
    return ''.join(b)
        
