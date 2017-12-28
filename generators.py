#!/usr/bin/env python3
"""
Generate some CSV files from online sources.
Copy,
http://www-01.sil.org/iso639-3/iso-639-3.tab
to
iso3.txt

attributation: www.sil.org/iso639-3/ 
"""
import os
import re
import codecs
from urllib import request


def langdataISO3():
    location='http://www-01.sil.org/iso639-3/iso-639-3.tab'
    data = request.urlopen(location)    
    content = data.read().decode('utf-8')

    languages = []
    for line in content.splitlines():
            data = line.split('\t')
            languages.append(data)
    return languages
  
def write_csv(basename, datalines):
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'csv', basename)
    with open(filename, 'w') as f:
        for l in datalines:
            f.write(l)
            f.write('\n')
        
    print("wrote {0} lines to '{1}'".format(len(datalines), basename))
          
def generate_all(filename=None):
    """
    Generate the language data
    """
    langdata = langdataISO3()
    lines = ['{0},{1},{2},{3},{4},{5},"{6}",{7}'.format(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]) for l in langdata]
    write_csv('languages_iso3.csv',  lines)



if __name__ == '__main__':
    print("Generating CSV files.")
    print("Please wait, this will take some time...")
    languages_lines = generate_all()
    print("Done.")
