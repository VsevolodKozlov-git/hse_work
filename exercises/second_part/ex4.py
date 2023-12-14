import re




def str_to_wordlist(string):
    return re.sub(r'[\W_\d]', ' ', string).split()


def main(string):
    elements = {}
    wordlist = str_to_wordlist(string)
    for word in wordlist:
        l = len(word)
        key = f'{l} letter words'
        if key not in elements:
            elements[key] = []
        elements[key].append(word)
    return elements

#elements = main(string)
