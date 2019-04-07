import json

JSON_FILE = 'detailed-list.json'
OUTPUT_JSON_FILE = 'e-contacts.json'

with open(JSON_FILE) as f:
    meps = json.loads(f.read())

data = {'*': {'#': 0}}

# collect keys
keys = ['#']
for mep in meps:
    for e_contact in mep['e_contacts']:
        if e_contact['type'] not in keys:
            keys.append(e_contact['type'])

# sort keys
keys = sorted(keys)
for key in keys:
    data['*'][key] = 0

for mep in meps:
    data['*']['#'] += 1
    data['*'][e_contact['type']] += 1

    if not mep['country'] in data:
        data[mep['country']] = {}
        for key in keys:
            data[mep['country']][key] = 0

    data[mep['country']]['#'] += 1
    for e_contact in mep['e_contacts']:
        data[mep['country']][e_contact['type']] += 1

with open(OUTPUT_JSON_FILE, 'w') as f:
    f.write(json.dumps(data, indent=2))
