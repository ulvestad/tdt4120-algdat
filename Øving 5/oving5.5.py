from sys import stdin

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
    # SKRIV DIN KODE HER
    li = []
    walked = []
    for weigth in xrange(len(nm[0])):
        if nm[0][weigth] ==  float(1e3000):
            continue
        else:
            li.append([nm[0][weigth],[0,weigth]])
    li.sort()
    walked.append(li[0])
    li.pop(0)
    b = walk(li, walked, nm) 
    return b

def walk(li, walked, nm):
    for weigth in xrange(len(nm)):
        if nm[walked[-1][1][1]][weigth]== float(1e3000):
            continue
        if nm[walked[-1][1][1]][weigth] == walked[-1][0]:
            continue
        else:
            li.append([nm[nm.index(nm[walked[-1][1][1]])][weigth],[nm.index(nm[walked[-1][1][1]]) ,weigth]])
    li.sort()
    walked.append(li[0])
    li.pop(0)
    while len(walked)<len(nm)-1:
        walk(li, walked, nm)
    walked.sort()
    return walked[-1][0]

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
