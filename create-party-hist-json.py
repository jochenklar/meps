import json
import operator

JSON_FILE = 'detailed-list.json'
OUTPUT_JSON_FILE = 'party.json'

with open(JSON_FILE) as f:
    meps = json.loads(f.read())

data = {'#': 0}

for mep in meps:
    data['#'] += 1
    if mep['national_political_group'] not in data:
        data[mep['national_political_group']] = 0
    data[mep['national_political_group']] += 1

data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)

with open(OUTPUT_JSON_FILE, 'w') as f:
    f.write(json.dumps(data, indent=2))
