"""Command line tool for reading json data.

Usage:

  jsonr <property name>*

"""

import json
import sys

def main():
  raw_content = sys.stdin.read()
  try:
    data = json.loads(raw_content)
  except ValueError:
    print(raw_content)
    raise

  for name in sys.argv[1:]:
    if isinstance(data, dict):
      data = data[name]
    elif isinstance(data, list):
      data = data[int(name)]
    else:
      print('%s (%s) is not subscriptable' % (data, type(data)))
      exit(1)

  if isinstance(data, (list, dict)):
    data = json.dumps(data)

  sys.stdout.write(str(data))

if __name__ == '__main__':
  main()
