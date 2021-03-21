import re

def _extract_price(value):
    match = re.match('^(.*?)([\d\.,]+)(.*)$', value)
    if match is None:
        raise ValueError("Can't extract price")
    return match.groups()


def _parse_price(price, thousand, decimal):
    trans = str.maketrans(decimal, '.', thousand)
    return float(price.translate(trans))


def parse_price(value):
    prefix, price, suffix = _extract_price(value)
    if '€' in prefix + suffix:
        thousand = '.'
        decimal = ','
    else:
        thousand = ','
        decimal = '.'
    return _parse_price(price, thousand, decimal)