from datetime import datetime
from unicodedata import normalize


def get_text(node, tag):
    try:
        return normalize('NFC', node.find(tag).text)
    except AttributeError:
        return None


def get_datetime(node, tag):
    text = get_text(node, tag)
    if text:
        return datetime.strptime(text, '%d/%m/%Y').strftime('%Y-%m-%d')
    else:
        return None


def get_attrib(node, tag, attrib):
    try:
        return normalize('NFC', node.find(tag).attrib[attrib])
    except AttributeError:
        return None
