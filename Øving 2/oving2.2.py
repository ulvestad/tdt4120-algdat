from sys import stdin
from collections import deque

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    depth = 0
    stack = []
    visit = []
    if rot.ratatosk:
        return depth
    current = rot
    while not current.ratatosk:
        if current not in visit:
            visit.append(current)
        for j in current.barn:
            stack.append(j)
        current = stack.pop()
    while True:
        if current == rot:
                return depth
        for x in visit:
            if current in x.barn:
                depth +=1
                current = x    
def bfs(rot):
    depth = 0
    queu = deque()
    visit = []
    if rot.ratatosk:
        return depth
    current = rot
    while not current.ratatosk:
        if current not in visit:
            visit.append(current)
        for j in current.barn:
            queu.append(j)
        current = queu.popleft()
    while True:
        if current == rot:
                return depth
        for x in visit:
            if current in x.barn:
                depth +=1
                current = x      
        

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print bfs(start_node)
    

