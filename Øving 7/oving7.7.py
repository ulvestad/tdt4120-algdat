from sys import stdin
from itertools import repeat

def m(result):
    # SKRIV DIN KODE HER
    word = ""
    for w in result:
        word+=w[1]
    return word

def merge(A):
    if len(A)<2:
        return A
    result =[]
    mid = int(len(A)/2)
    left = merge(A[:mid])
    right = merge(A[mid:])
    i = 0
    j =0
    while len(left)> i and len(right)> j:
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    result += left[i:]
    result += right[j:]
    return result

def main():
    decks = []
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        for x in deck:
           decks.append(x)
    li = []
    li = merge(decks)
    print m(li)
main()
