import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')
def printGraph(g,n):
    for i in range(n):
        for j in range(n):
            print(g[i][j],end=" ")
        print()

def floydWarsall(graph,n,p):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k]<float('inf') and  graph[k][j]<float('inf'):#handle negative weight
                    graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
                    p[i][j]=k

n=int(input())
graph=[[0 for i in range(n)] for j in range(n)]
for _ in range(n):
    u,v,w=map(int,input().split())
    graph[u][v]=w
for i in range(n):
    for j in range(n):
        if i==j:
            graph[i][j]=0
        elif graph[i][j]==0:
            graph[i][j]=float('inf')
p=[[0 for i in range(n)] for j in range(n)]
floydWarsall(graph,n,p)
printGraph(graph,n)
print()
printGraph(p,n)
