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
    if indeks >= len(ord): #sjekker om indeks er lik/større enn ordet
        return node.posi #hvis så returner node pos
    l = ord[indeks] #bokstavene er ord med indeks n
    if l in node.barn: # hvis bokstaven er i nodens barn
        return posisjoner(ord, indeks+1, node.barn[l]) #kjører rekusrsivt til gjennom ordet og returnerer pos
    if l == '?':#hvis bokstav er ?
        pos = [] #lag tom liste
        for x in node.barn.keys(): #for hver node sine barn sine nøkler 
            pos += (posisjoner(ord, indeks+1, node.barn[x]))#kall reukrsivt og legg til posisjon
        return pos#returnerer lista med posisjoner
    else:
        return [] #returnerer tom liste dersom ingen noden ikke er gydlig
def m():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append( (o,pos) )
            pos += len(o) + 1
        toppnode = bygg(ordliste)
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
m()
