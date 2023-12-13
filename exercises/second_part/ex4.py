import re
from collections import defaultdict



def str_to_wordlist(string):
    return re.sub(r'[\W_\d]', ' ', string).split()


def main(string):
    elements = defaultdict(list)
    wordlist = str_to_wordlist(string)
    for word in wordlist:
        l = len(word)
        key = f'{l} letter words'
        elements[key].append(word)
    return elementse