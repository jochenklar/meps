import urllib.request
import xml.etree.ElementTree as et

BASE_URL = 'http://www.europarl.europa.eu/meps/en/odp/detailed-list-xml/'
XML_FILE = 'detailed-list.xml'

xml = None
for letter in map(chr, range(97, 123)):
    url = BASE_URL + letter
    print(url)

    response = urllib.request.urlopen(url)
    data = response.read().decode()
    root = et.fromstring(data)

    if xml:
        for element in root:
            xml.append(element)
    else:
        xml = root

et.ElementTree(xml).write(XML_FILE)
