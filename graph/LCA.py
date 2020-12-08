import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')



n=int(input())
parent=[sys.maxsize-1]*(n+1)
parent[0]=-1
graph=[[] for i in range(n+1)]

for _ in range(n):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

'''     Naive approach
        the complexity of each querry is o(n)
        input:
        
            9
            0 1
            0 7
            1 2
            1 3
            1 6
            3 4 
            3 5
            7 8
            7 9

 
'''

def getParent(graph,node,par):
    for i in range(len(graph[node])):
        if graph[node][i]!=par:
            parent[graph[node][i]]=node
            getParent(graph,graph[node][i],node)


def lca(u,v,root):
    visited=[False]*(n+1)
    #traverse from u to root node and mark true all nooe
    lca=-1
    while True:
        visited[u]=True
        if u==root:
            break 
        u=parent[u]
    
    #traverse from v until we get first visited node
    while True:
        if visited[v]:
            lca=v 
            break
        v=parent[v]
        
    return lca 






print(graph)
getParent(graph,0,-1)
print(parent)
print(lca(4,5,0))