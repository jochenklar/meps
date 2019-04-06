from datetime import datetime
from unicodedata import normalize


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
