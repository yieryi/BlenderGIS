import os, ssl

import logging
log = logging.getLogger(__name__)

import json

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import quote_plus

TIMEOUT = 2

def nominatimQuery(
    query,
    base_url = 'https://restapi.amap.com/v3/geocode/geo?',
    referer = None,
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    format = 'JSON',
    limit = 10):

    # url = base_url + 'search?'
    url = base_url + 'key=6a5c612bf543701c5ebbfde318830722'
    url += '&format=' + format
    url += '&address=' + quote_plus(query)
    # url += '&limit=' + str(limit)

    log.debug('Nominatim search request : {}'.format(url))

    req = Request(url)
    if referer:
        req.add_header('Referer', referer)
    if user_agent:
        req.add_header('User-Agent', user_agent)

    response = urlopen(req, timeout=TIMEOUT)

    r = json.loads(response.read().decode('utf-8'))

    return r
