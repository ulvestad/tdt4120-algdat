from sys import stdin, stderr

# kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
# startrom er en liste med indeksene til nodene som tilsvarer startrommene.
# utganger er en liste med indeksene til nodene som tilsvarer utgangene.

def antallIsolerteStier(flow,kapasiteter, startrom, utganger):
    # Du kan bruke metoden finnFlytsti for aa forenkle oppgaven.
    # SKRIV DIN KODE HER
    counter = 0
    for start in startrom:
        p = finnFlytsti(start, utganger, flow, kapasiteter)
        for i in xrange(len(p)-1):
            flow[p[i]][p[i+1]] += 1
            flow[p[i+1]][p[i]] -= 1
            
        if len(p) > 0: counter+=1
    print counter    

# Finner en sti fra noden med indeks 'kilde' til noden med indeks 'sluk'
# med ledig kapasitet i et flytnettverk med flyt F og kapasitet C.
# Returnerer en liste hvor foerste element er indeksen til en av startnodene, 
# siste element er indeksen til en av utgangene, og elementene imellom er 
# indeksene til de andre nodene paa veien som ble funnet, i riktig rekkefoelge.
# Eksempel: en sti fra startnoden 4 til node 3, node 9, node 7 og til slutt til 
# utgangen 12 vil representeres som [4, 3, 9, 7, 12].

def finnFlytsti(kilde, sluk, F, C):
    n = len(F)
    oppdaget, forelder, koe = [False]*n, [None]*n, [kilde]

    while koe:
        node = koe.pop(0)
        
        for nabo in range(n):
            if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                if nabo in utganger:
                    sti = [nabo, node]
                    while node != kilde:
                        node = forelder[node]
                        sti.append(node)
                    sti.reverse()
                    return sti
        
                koe.append(nabo);
                oppdaget[nabo] = True
                forelder[nabo] = node
    return []

noder = [int(x) for x in stdin.readline().split()]
startrom = [int(x)*2 for x in stdin.readline().split()]
utganger = set([int(x)*2+1 for x in stdin.readline().split()])
nabomatrise, flyt = [], []

for i in xrange(noder[0]*2):
    flyt.append([0]*(noder[0]*2))
    nabomatrise.append([0]*(noder[0]*2))
    
for k in xrange(noder[0]):
    temp = stdin.readline().split(' ')
    nabomatrise[2*k][2*k+1] = 1
    for j in xrange(noder[0]):
        nabomatrise[k*2+1][j*2] = int(temp[j])

print antallIsolerteStier(flyt, nabomatrise, startrom, utganger)