# This module is highly customized for plan requirements on uWaterloo calendars
# that are generated dynamically

from bs4 import BeautifulSoup
import re

def parse (html_source):
    # Get all tags in the main content table
    # All the beefy stuff :D
    tree = BeautifulSoup(html_source, 'html.parser')
    span = tree.find_all('span', {'class': 'MainContent'})
    tags = span[0]
    
    # These are the tags we want to keep
    LOOK_FOR = ['p', 'blockquote']
    relevant_tags = [ e for e in tags if e.name in LOOK_FOR ]

    # Start parsing
    # We may want to keep descriptions and information such as conditions that 
    #   the courses. e.g. 'One of', 'Three additional...'
    return extract_text_from_blockquote( 
            [ e for e in relevant_tags if e.name == 'blockquote' ] )

def extract_text_from_blockquote (blockquotes):
    # Input is a list of blockquote tags
    results = []
    course_code_re = re.compile('^[A-Z]{2,6}\s[0-9]{2,4}')
    for bq in blockquotes:
        for node in bq:
            if node.name in ['a', 'p'] and course_code_re.match(node.string):
                results.append(node.string)
            else:
                text = node.string
                if text is not None and course_code_re.match(text.strip()):
                    results.append(text.strip())

    # Remove white space
    return [e for e in results if is_not_whitespace(e)]

def is_not_whitespace(s):
    ws = ['\n', '']
    return s not in ws
