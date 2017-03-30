#!/usr/bin/python

from uw import parse
import requests
import sys

def parse_html (url):
    page = requests.get(url)

    # HTML source passed as bytes
    return uw.parse(page.content)

if __name__ == '__main__':
    return parse_html(sys.argv[1])
