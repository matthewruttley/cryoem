"""
  analysis
  ~~~~~~~~~~~~
  Gets specific fields from an XML file and saves
  them to a SQL file.

  Usage:
    - Modify the SQL/xml_data.sql file to have fields and datatypes
    that match the useful_fields list below
    - Expand the useful_fields list below to have the keys you want
    - Run analysis.py
    - run psql -f output.sql
    - Inspect in DB

"""

from collections import defaultdict
import os

import xmltodict

useful_fields = [
  ['admin_date', ['emd', 'admin', 'current_status', 'date']],
  # Add cols to pick out here
]

def get_value(d, path):
  if len(path) == 1:
    return d[path[0]]
  else:
    return get_value(d[path[0]], path[1:])


def build_analysis():
  """handler"""
  
  xml_data = {}
  
  for fn in os.listdir('XML'):
    if 'v30' in fn:
      with open('XML/' + fn) as f:
        contents = xmltodict.parse(f.read())

        values = []
        for col_name, path in useful_fields:
          values.append(get_value(contents, path))

        xml_data[fn] = values
  
  # Convert to SQL
  with open('SQL/xml_data.sql') as f:
    sql = f.read()

  for fn, vals in xml_data.iteritems():

    # Hackish implementation here:
    inserts = ""
    for x in vals:
      if isinstance(x, basestring):
        inserts += "'{}', ".format(x.replace("'", ""))
      else:
        inserts += "{}, ".format(x) # numbers
    sql += "('{}', {}),".format(fn, inserts[:-2])
    
  sql = sql[:-1] + '\n;'

  # Save file
  with open('output.sql', 'w') as f:
    f.write(sql)

if __name__ == '__main__':
  build_analysis()
