import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')
from collections import defaultdict


graph=defaultdict(list)
def addEdges(u,v):
    graph[u].append(v)
def dfs(u,visited,st):
    visited[u]=True

    for c in graph[u]:
        if visited[c]==False:
            dfs(c,visited,st)
    st.append(u)

def main():
    n,m=map(int,input().split())
    for _ in range(m):
        u,v=map(int,input().split())
        addEdges(u,v)
    visited=[False]*(n+1)
    st=[]
    for i in range(n):
        if not visited[i]:
            dfs(i,visited,st)
    print(graph)
    print(st[::-1])

main()