import json
import requests
import time

NOMATIM_URL = 'https://nominatim.openstreetmap.org/search.php'

JSON_FILE = 'detailed-list.json'
OUTPUT_JSON_FILE = 'birthplace.json'

with open(JSON_FILE) as f:
    meps = json.loads(f.read())

geojson = {
  'type': 'FeatureCollection',
  'features': []
}

for mep in meps:
    print(mep['full_name'], mep['birth_place'])

    time.sleep(1)

    response = requests.get(url=NOMATIM_URL, params={
        'q': mep['birth_place'],
        'format': 'json'
    })

    try:
        response_data = response.json()
    except json.decoder.JSONDecodeError:
        print('!')
        continue

    if response_data:
        geojson['features'].append({
            'id': mep['id'],
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    float(response_data[0]['lon']),
                    float(response_data[0]['lat'])
                ]
            },
            'properties': mep
        })

with open(OUTPUT_JSON_FILE, 'w') as f:
    f.write(json.dumps(geojson, indent=2))
