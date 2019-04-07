import re

from datetime import datetime
from unicodedata import normalize

pattern = re.compile(r'(\(.*\))|(\S+)')


def get_text(node):
    try:
        return normalize('NFC', node.text)
    except AttributeError:
        return None


def get_datetime(node):
    text = get_text(node)
    if text:
        return datetime.strptime(text, '%d/%m/%Y').strftime('%Y-%m-%d')
    else:
        return None


def get_attrib(node, attrib):
    try:
        return normalize('NFC', node.attrib[attrib])
    except AttributeError:
        return None


def parse_full_name(full_name):
    first_names = []
    last_names = []

    words = []
    for group in pattern.findall(full_name):
        a, b = group
        words.append(a if a else b)

    for word in words:
        if word.isupper():
            last_names.append(word.title())
        else:
            if word.startswith('Mc') and word[2:].isupper():
                last_names.append('Mc' + word[2:].title())
            else:
                first_names.append(word)

    return first_names, last_names

