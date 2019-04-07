import json

from unicodedata import normalize
from xml.etree import ElementTree as et

from utils import get_text, parse_full_name

XML_FILE = 'directory.xml'
JSON_FILE = 'directory.json'

xml = et.parse(XML_FILE)

mep_data = []
mep_nodes = xml.findall('mep')
for mep in mep_nodes:
    full_name = get_text(mep.find('fullName'))
    first_names, last_names = parse_full_name(full_name)

    mep_data.append({
        'id': get_text(mep.find('id')),
        'full_name': full_name,
        'first_names': first_names,
        'last_names': last_names,
    })

with open(JSON_FILE, 'w') as f:
    f.write(normalize('NFC', json.dumps(mep_data, indent=2)))
