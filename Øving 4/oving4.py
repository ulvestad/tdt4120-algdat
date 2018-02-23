from sys import *


def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    li = [startnode]
    if startnode < 0:
        li = [startnode]
    else:
        k =-1
        for node in nabomatrise[startnode]:
            k+=1
            if node and k not in li:
                li.append(k)
        notvisit = []
        print li
        for x in xrange(len(nabomatrise)):
            if x not in li:
                notvisit.append(x)
        print notvisit
        noder = len(notvisit)
        kanter = 0
        for i in notvisit:
            for x in xrange(len(nabomatrise[i])):
                if nabomatrise[i][x] and x in notvisit:
                    kanter+=1
        print noder
        print kanter
        if noder == 0:
            return 0.0 
        if n == 0:
            return 0.0
        return float(kanter) / float(noder**2)

def main():
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
main()
