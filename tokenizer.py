"""
This was heavily inspired from the Python Cookbook, 3rd Edition
David Beazley & Brian K. Jones
"""
import re
import sys
from collections import namedtuple


# Token Specification
NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
    
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Pass a file name as the command line arg to this file.")
    else:
        name = sys.argv[1]
        openfile = open(name, 'r')
        data = openfile.read()
        openfile.close()
        tokens = (tok for tok in generate_tokens(master_pat, data) if tok.type != 'WS')
        for tok in tokens:
            print(tok)
