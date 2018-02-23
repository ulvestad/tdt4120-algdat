# -*- coding: cp1252 -*-
from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    rot = Node()
    current = rot
    for x in ordliste:
        for i in range(len(x[0])):
            char = x[0][i]
            if char in current.barn: # har bokstaven/noden barn
                current = current.barn[char] #endre naverende node til neste barn
            else:
                current.barn[char] = Node() #sett noden til rotnode
                current = current.barn[char] #endre naverende node til neste barn
            if i == len(x[0])-1: #hvis det er siste bokstav i ordet
                current.posi.append(x[1]) #legg til pososijonen til naverende node
        current = rot #setter naverende til rot for neste ord
    return rot


def posisjoner(ord, indeks, node):
    if indeks >= len(ord):
        return node.posi
    if ord[indeks] in node.barn:
        return posisjoner(ord, indeks+1, node.barn[ord[indeks]])
    if ord[indeks] == '?':
        pos = []
        for x in node.barn.keys():
            pos += (posisjoner(ord, indeks+1, node.barn[x]))
        return pos
    else:
        return []

def printTree(node):
    for key in node.barn.keys():
        print key, ':', node.barn[key].posi
        printTree(node.barn[key])

try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    printTree(toppnode)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)
