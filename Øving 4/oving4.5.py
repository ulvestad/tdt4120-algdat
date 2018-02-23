from sys import *

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    li = [startnode]
    li= trav(nabomatrise, startnode, li)
    notvisit = []
    for x in xrange(len(nabomatrise)):
        if x not in li:
            notvisit.append(x)
    noder = len(notvisit)
    kanter = 0
    for i in notvisit:
        for x in xrange(len(nabomatrise[i])):
            if nabomatrise[i][x] and x in notvisit:
                kanter+=1         
    if noder == 0:
        return 0.0 
    if n == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)

def trav(nabomatrise, startnode, li):
    if startnode < 0:
        return []
    else:
        n = -1
        for node in nabomatrise[startnode]:
            n+=1
            if node and n not in li:
                li.append(n)
                trav(nabomatrise, n, li)
        return li

def init():
    n = int(stdin.readline())
    nabomatrise = [None] * n
    for i in range(0, n):
        nabomatrise[i] = [False] * n 
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
init() 
