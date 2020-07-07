## Code Review
---
'if not string != string' seem like a double negitive where I would think
'''
  if string != string:
    try:
      found = pattern.search(str(string))
      ...
'''

for clarity I would just change comment on convert_time() to be
'# Expect a dataframe colum and convert time to second format'

Everythingwas really clean and easy to read. Honestly I won't have any comment and had to be picky to have something to write about. 