from sys import stdin
from itertools import repeat

def merge(decks):
    # SKRIV DIN KODE HER
    result = []
    for deck in decks:
        if len(deck)<2:
            result.append(deck[0])
        else:
            for x in deck:
                result.append(x)
    result = sort(result)        
    word = ""
    for w in result:
        word+=w[1]
    return word

def sort(deck):
    for index in xrange(1, len(deck)):
        value = deck[index]
        pos = index
        while pos>0 and deck[pos-1]>value:
            deck[pos] = deck[pos-1]
            pos = pos-1
        deck[pos] = value
    return deck

def main():
    decks = []
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        decks.append(deck)
    print merge(decks)
main()
