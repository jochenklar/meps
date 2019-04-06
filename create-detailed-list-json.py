import json

from xml.etree import ElementTree as et

from utils import get_text, get_datetime, get_attrib

XML_FILE = 'detailed-list.xml'
JSON_FILE = 'detailed-list.json'

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
        'country': get_text(mep, 'country'),
        'country_code': get_attrib(mep, 'country', 'countryCode'),
        'political_group': get_text(mep, 'politicalGroup'),
        'political_group_code': get_attrib(mep, 'politicalGroup', 'bodyCode'),
        'national_political_group': get_text(mep, 'nationalPoliticalGroup'),
        'national_political_group_code':  get_attrib(mep, 'nationalPoliticalGroup', 'bodyCode'),
        'birth_date': get_datetime(mep, 'birthDate'),
        'birth_place': get_text(mep, 'birthPlace'),
    })

with open(JSON_FILE, 'w') as f:
    f.write(json.dumps(mep_data, indent=4))
