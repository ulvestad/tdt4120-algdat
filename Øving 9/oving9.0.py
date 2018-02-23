from sys import stdin, stderr

# kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
# startrom er en liste med indeksene til nodene som tilsvarer startrommene.
# utganger er en liste med indeksene til nodene som tilsvarer utgangene.

def antallIsolerteStier(kapasiteter, startrom, utganger):
    # Du kan bruke metoden finnFlytsti for aa forenkle oppgaven.
    # SKRIV DIN KODE HER
    maxflow = 0
    nodes_used = [0 for n in kapasiteter]
    n = len(kapasiteter)
    F= [[0 for x in xrange(n)]for x in xrange(n)] 
    for start in startrom:
        for utgang in utganger:
            path = finnFlytsti(start, utgang, F, kapasiteter, nodes_used)
            if not path:
                continue
            #for flyt in xrange(len(path)-1):
                    #F[path[flyt]][path[flyt+1]] = 1
            #for i in range(len(path)):
                #if path[i] in (item for sublist in paths for item in sublist):
                    #None
            for x in range(len(path) - 1):
                i = path[x]
                j = path[x+1]
                nodes_used[i] = 1
                nodes_used[j] = 1
                F[i][j] = 1
                F[j][i] = 1      
            maxflow +=1 
    return maxflow
        

# Finner en sti fra noden med indeks 'kilde' til noden med indeks 'sluk'
# med ledig kapasitet i et flytnettverk med flyt F og kapasitet C.
# Returnerer en liste hvor foerste element er indeksen til en av startnodene, 
# siste element er indeksen til en av utgangene, og elementene imellom er 
# indeksene til de andre nodene paa veien som ble funnet, i riktig rekkefoelge.
# Eksempel: en sti fra startnoden 4 til node 3, node 9, node 7 og til slutt til 
# utgangen 12 vil representeres som [4, 3, 9, 7, 12].

def finnFlytsti(kilde, sluk, F, C, used):
    n = len(F)
    oppdaget = [False] * n
    forelder = [None] * len(F)
    koe = [kilde]
    while koe:
        node = koe.pop(0)
        if node == sluk:
            # Har funnet sluken, lager en array med passerte noder
            sti = []
            i = node
            while True:
                sti.append(i)
                if used[i] == 1:
                    return None
                if i == kilde:
                    break
                i = forelder[i]
            sti.reverse()
            return sti;
        for nabo in range(n):
            if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                koe.append(nabo);
                oppdaget[nabo] = True;
                forelder[nabo] = node;
    return None

def main():
    noder, _, _ = [int(x) for x in stdin.readline().split()]
    startrom = [int(x) for x in stdin.readline().split()]
    utganger = [int(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [int(nabo) for nabo in linje.split()]
        nabomatrise.append(naborad)
    print antallIsolerteStier(nabomatrise, startrom, utganger)
main()