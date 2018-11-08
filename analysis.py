"""
  Analyze XML files
"""

from collections import defaultdict

from converter import xml_to_json # todo find module

useful_fields = [
  ['admin_date', ['emd', 'admin', 'current_status', 'date']]
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
        contents = xml_to_json(f.read())

        values = []
        for col_name, path in useful_fields.iteritems():
          values.append(get_value(contents, path))

        xml_data[fn] = values
  
  # Convert to SQL
  with open('SQL/xml_data.sql') as f:
    sql = f.read()

  for fn, vals in xml_data.iteritems():
    vals = tuple([fn] + vals)
    sql += '{},'.format(repr(tuple)) # Check that this works with no unicode errors
  sql = sql[:-1] + ';'

  # Save file
  with open('output.sql', 'w') as f:
    f.write(sql)

if __name__ == '__main__':
  analyze()
