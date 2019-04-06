import json

from unicodedata import normalize
from xml.etree import ElementTree as et

from utils import get_text, get_attrib, get_datetime

XML_FILE = 'detailed-list.xml'
JSON_FILE = 'detailed-list.json'

xml = et.parse(XML_FILE)

mep_data = []
mep_nodes = xml.findall('mep')
for mep in mep_nodes:
    full_name = get_text(mep.find('fullName'))
    mep_data.append({
        'id': get_text(mep.find('id')),
        'full_name': full_name,
        'first_names': [word.title() for word in full_name.split() if not word.isupper()],
        'last_names': [word.title() for word in full_name.split() if word.isupper()],
        'country': get_text(mep.find('country')),
        'country_code': get_attrib(mep.find('country'), 'countryCode'),
        'political_group': get_text(mep.find('politicalGroup')),
        'political_group_code': get_attrib(mep.find('politicalGroup'), 'bodyCode'),
        'national_political_group': get_text(mep.find('nationalPoliticalGroup')),
        'national_political_group_code':  get_attrib(mep.find('nationalPoliticalGroup'), 'bodyCode'),
        'birth_date': get_datetime(mep.find('birthDate')),
        'birth_place': get_text(mep.find('birthPlace')),
        'e_contact': [{
            'type': get_attrib(econtact, 'type'),
            'address': get_text(econtact)
        } for econtact in mep.findall('eContact')]
    })

with open(JSON_FILE, 'w') as f:
    f.write(normalize('NFC', json.dumps(mep_data, indent=2)))
