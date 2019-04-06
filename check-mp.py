import json

LAST_NAME = 'Keller'
FIRST_NAME = 'Ska'
JSON_FILE = 'detailed-list.json'

with open(JSON_FILE) as f:
    meps = json.loads(f.read())

for mep in meps:
    if LAST_NAME in mep['last_names'] and FIRST_NAME in mep['first_names']:
        break

print(FIRST_NAME + ' ' + LAST_NAME, mep.get('national_political_group_code'))
