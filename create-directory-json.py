import json

from xml.etree import ElementTree as et

from utils import get_text

XML_FILE = 'directory.xml'
JSON_FILE = 'directory.json'

xml = et.parse(XML_FILE)

mep_data = []
mep_nodes = xml.findall('mep')
for mep in mep_nodes:
    full_name = get_text(mep, 'fullName')

    mep_data.append({
        'id': get_text(mep, 'id'),
        'full_name': full_name,
        'first_names': [word.title() for word in full_name.split() if not word.isupper()],
        'last_names': [word.title() for word in full_name.split() if word.isupper()],
    })

with open(JSON_FILE, 'w') as f:
    f.write(json.dumps(mep_data, indent=4))
