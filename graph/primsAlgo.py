import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')
from collections import defaultdict
#to implement prims algo
# visisted[]
#weight[]
#parent
graph=defaultdict(list)
def prims(n,weight,parent,visited):
    for i in range(n):
        if visited[i]==False:
            visited[i]=True 

        for c in graph[i]:
            for x,y in c.items():
                weight[x]=min(weight[x],y)
                parent[x]=i
    print(weight)

def main():
    n,m=map(int,input().split())
    #wt=list(map(int,input().split()))
    for _ in range(m):
        m1={}
        m2={}
        u,v,w=map(int,input().split())
        m1[v]=w
        m2[u]=w  

        graph[u].append(m1)
        graph[v].append(m2)

    visited=[False]*(n+1)
    parent=[-1]*n 
    weight=[sys.maxsize-1]*n 
    weight[0]=0
    prims(n,weight,parent,visited)
    print(graph)
main()