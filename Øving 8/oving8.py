from sys import stdin, stderr

def beste_sti(nm, sans):
    # SKRIV DIN KODE HER
    n = len(sans)
    done_path = [False] * n
    best_sans = [0.0] * n 
    best_sans[0] = sans[0]
    prev = range(n)
    best_node = 0
    for i in range(n):
        node =	best_node
        done_path[node] = True
        biggest_best_sans = -1.0
        for nabo in range(n):
            if not done_path[nabo]:
                if nm[node][nabo]:
                    offer = best_sans[node] * sans[nabo]
                    if offer > best_sans[nabo]:
                        prev[nabo] = node
                        best_sans[nabo] = offer
                if best_sans[nabo] > biggest_best_sans:
                   	best_node = nabo
                   	biggest_best_sans = best_sans[nabo]
    if(best_sans[-1] == 0.0):
        return '0'
    index = n - 1
    path = []
    while index != 0:
        path.append(index)
        index = prev[index]
    path.append(0)
    best_path = []
    while path:
    	best_path.append(path.pop())
    string_path = ""
    for x in xrange(len(best_path)):
    	if x == 0:
    		string_path+= str(best_path[x])
    	else:
    		string_path+="-"+str(best_path[x])
    return string_path;

def main():

	n = int(stdin.readline())
	sannsynligheter = [float(x) for x in stdin.readline().split()]
	nabomatrise = []
	for linje in stdin:
	    naborad = [0] * n
	    naboer = [int(nabo) for nabo in linje.split()]
	    for nabo in naboer:
	        naborad[nabo] = 1
	    nabomatrise.append(naborad)
	print beste_sti(nabomatrise, sannsynligheter)
main()