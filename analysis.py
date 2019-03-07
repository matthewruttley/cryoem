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

from searchterms.searchterms import useful_fields 

def get_value(d, path, f):
  """
    Takes the path and iterates over it.
  """
  try:
    if len(path) == 1:
      if len(d[path[0]]) == 2:
        try:
          return d[path[0]].items()[1][1] # This captures the detector mode for some weird xml files.
        except AttributeError:
          pass
      else:
        return d[path[0]]
    else:
      return get_value(d[path[0]], path[1:], f)
  except TypeError:
    pass

def build_analysis():
  """handler"""
  
  xml_data = {}
  
  for fn in os.listdir('XML/'):
    if 'swp' not in fn:
      with open('XML/' + fn) as f:
        contents = xmltodict.parse(f.read())

        values = []
        for col_name, path in useful_fields:
          try:
            values.append(get_value(contents, path, f))
          except KeyError, TypeError:
            values.append(str('NULL')) 
        xml_data[fn] = values
  
  # Convert to SQL
  with open('SQL/xml_data.sql') as f:
    sql = f.read()

  for fn, vals in xml_data.iteritems():

    # Hackish implementation here:
    inserts = ""
    for x in vals:
      try:
        if isinstance(x, basestring):
          inserts += "'{}', ".format(x.replace("'", ""))
        else:
          inserts += "{}, ".format(x) # numbers
      except UnicodeEncodeError:
        pass
    sql += "('{}', {}),".format(fn, inserts[:-2])
    
  sql = sql[:-1] + '\n;'

  # Save file
  with open('output.sql', 'w') as f:
    f.write(sql)

if __name__ == '__main__':
  build_analysis()
