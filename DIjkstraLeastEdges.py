class Modify():
    def __init__(self):
        self.size = 0
        self.S = []
    def notempty(self):
        return self.size     
    def vertexaddn(self,Vertex1):
        self.S.append(Vertex1)
        self.size += 1
    def extractmin(self):
        if self.notempty:
            self.size -= 1
            return self.S.pop(0)
        return -1
    def update(self,nodeUpdation):
        priority = self.S.index(nodeUpdation)
        while priority > 0:
            if G[self.S[priority]][1] <  G[self.S[priority//2]][1]:
                t = self.S[priority]
                self.S[priority] = self.S[priority//2]
                self.S[priority//2] = t
            priority = priority // 2

#Taking input from user

vert11, edge1 = input().split()
vert11=int(vert11)
edge1=int(edge1)

edge2=[]
for i in range(edge1):
        edge3=[]      
        a,b,c=input().split()
        a=int(a)
        b=int(b)
        c=int(c)
        edge3.append(a)
        edge3.append(b)
        edge3.append(c)
        edge2.append(edge3)
source, destination = input().split()
source=int(source)
destination=int(destination)

heap = Modify()

#Initializing the graph
G=[]  #G is an empty graph
for name in range(0, vert11):
    graph1=[]
    graph1.append(name)
    graph1.append(100000)
    graph1.append(-1)
    graph1.append(100000)
    graph1.append(-1)
    G.append(graph1)

for k in range(len(G)):
    for j in range(k+1):
        G[j][4]=G[k][0]
    if(G[k][0] == source):
        G[j][1] = 0
        G[j][2] = 0
        G[j][3] = -1
        heap.vertexaddn(G[j][0])
        break    

Result = []

for vertex in G: 
    if vertex[0] != source:
        heap.vertexaddn(vertex[0])
p=[]
def relaxops(interSrc,interDest,weight):
    
    if interDest[1] > interSrc[1] + weight:
        interDest[1] = interSrc[1] + weight
        interDest[2] = interSrc[0]
        interDest[3] = interSrc[3] + 1
        
        p.append(interSrc[0])
        p.append(interDest[0])
    elif interDest[1] == interSrc[1] + weight:
        if interDest[3] > interSrc[3] + 1:
            interDest[2] = interSrc[0]
            interDest[3] = interSrc[3] + 1
            p.append(interSrc[0])
            p.append(interDest[0])
        elif interDest[3] == interSrc[3] + 1:
                i = interDest[3] -1
                p.append(interSrc[0])
                p.append(interDest[0])
                point1 = interDest[2]
                point2 = interSrc[0]
                while (i > 0):
                    point1 = G[point1][2]
                    point2 = G[point2][2]
                    i -= 1
                    interDest[2] = interSrc[0]
                    
    print(p)
    heap.update(interDest[0])
    
while heap.notempty():
    u = heap.extractmin()
    Result.append(u)
    i = 0
    while i < len(edge2):
        edge = edge2[i]
        if edge[0] == G[u][0] or edge[1] == G[u][0]:
            if edge[0] == G[u][0]:
                relaxops(G[edge[0]],G[edge[1]],edge[2])
                edge2.pop(i)
            else:
                relaxops(G[edge[1]],G[edge[0]],edge[2])
                edge2.pop(i)
        else:
            i += 1
'''
if(len(Graph)==1):
    print(0, end=" ")
    print(Graph[0][0])
'''    
dest = destination
path = list([])
cnt = 0
while G[dest][0] != G[source][0]  :
    path.insert(0,G[dest][0])
    if cnt > 10:
        break
    cnt = cnt + 1
    dest = G[dest][2]
path.insert(0,source)
print(G[destination][1])
for i in range(0,len(path)-1):
    print(path[i],end = " ")
print(destination)
