from sys import stdin

def mst(nm):
    min_tree = prim(nm)
    biggest = 0
    for i,j in min_tree:
       if nm[i][j]> biggest:
           biggest = nm[i][j] 
    return biggest

def prim(nm):
    Inf = float(1e3000)
    nodes = len(nm)
    notfound = []
    for x in xrange(len(nm)-1):
        notfound.append(x+1)
    tree = []
    bneigbour = [None]*nodes
    bprice = [Inf]*nodes 
    prev = 0
    while len(notfound) > 0:
        for i in notfound:
            if nm[i][prev] < bprice[i]:
                bneigbour[i] = prev
                bprice[i] = nm[i][prev]
        mprice = Inf
        for i in notfound:
            if bprice[i] < mprice:
                nextfrom = i
                nextto = bneigbour[i]
                mprice = bprice[i]
        tree.append((nextfrom, nextto))
        notfound.remove(nextfrom)
        prev = nextfrom
    return tree

def init():
    Inf = float(1e3000)
    False = 0
    True = 1
    linjer = []
    for str in stdin:
        linjer.append(str)
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = [Inf] * n
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node][nabo] = vekt
        node += 1
    print mst(nabomatrise)
init()
