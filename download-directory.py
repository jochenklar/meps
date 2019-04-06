import urllib.request

URL = 'http://www.europarl.europa.eu/meps/en/directory/xml'
XML_FILE = 'directory.xml'

response = urllib.request.urlopen(URL)

with open(XML_FILE, 'w') as f:
    f.write(response.read().decode())
