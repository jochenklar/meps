import json
from unicodedata import normalize

MEPS = 'Albiol Guzmán, Benito Ziluaga, Björk, Chrysogonos, Eck, Ernst, Flanagan, González Peñas, Hadjigeorgiou, Händel, Kari, Kohlíček, Konečná, López Bermejo, Lösing, Maštálka, Matias, Michels, Sakorafa, Sánchez Caldentey, Schirdewan, Scholz, Spinelli, Urbán Crespo, Zimmer'

JSON_FILE = 'detailed-list.json'

with open(JSON_FILE) as f:
    meps = json.loads(f.read())


def search_mep(full_name):
    names = full_name.strip().split(' ')

    for mep in meps:
        mep_names = mep['last_names'] + mep['first_names']
        if set(names).issubset(mep_names):
            return mep


for full_name in normalize('NFC', MEPS).split(','):
    mep = search_mep(full_name) or {}
    print(full_name.strip(), mep.get('national_political_group_code'))
