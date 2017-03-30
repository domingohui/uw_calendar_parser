#!/usr/bin/python

import uw
import requests
import sys

def parse_html (url):
    page = requests.get(url)

    # HTML source passed as bytes
    return uw.parse(page.content)

if __name__ == '__main__':
    print(parse_html(sys.argv[1]))
