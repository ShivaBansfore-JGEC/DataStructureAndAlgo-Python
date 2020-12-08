import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')


def bellmanford(src,v):
    dist=[float('inf')]*(v) #taking a distance array of size v no of vetex
    dist[src]=0
    for _ in range(v-1):
        for u,v,w in graph:
            if dist[u]!=float('inf') and dist[u]+w < dist[v]:
                dist[v]=dist[u]+w

    for u,v,w in graph:
        if dist[u]!=float('inf') and dist[u]+w < dist[v]:
            print('it has negative cycle')
            return 
    
    for i in range(len(dist)):
        print(i,"-->",dist[i])

V,e=map(int,input().split())
graph=[]
for _ in range(e):
    sub=[]
    u,v,w=map(int,input().split())
    sub.append(u)
    sub.append(v)
    sub.append(w)
    graph.append(sub)
bellmanford(0,V)
