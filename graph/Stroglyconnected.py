import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')
from collections import defaultdict
#   KOSARAJU'S ALGO
'''
  step1: sort graph according to finishing time 
  step2: transpose the graph
  step3: dfs on each vertex

  input:
        5 5
        1 4
        1 2
        2 3
        3 1
        4 5
'''

graph={}
def dfs(u,visited):
    visited[u]=True
    print(u,end=" ") 
    for c in graph[u]:
        if visited[c]==False:
            dfs(c,visited)
        
# step 1: sorting according to finishing time 
def sort_graph(u,visited,st):
    visited[u]=True
    for i in graph[u]:
        if visited[i]==False:
            sort_graph(i,visited,st)
    st.append(u)

# step2: transpose the graph 
tg=defaultdict(list)
def transpose_graph():
    for x,y in graph.items():
        for j in y:
            tg[j].append(x)
    print(tg)

# step3: reverse dfs
def revDfs(u,visited):
    visited[u]=True 
    print(u,end=" ")
    for c in tg[u]:
        if visited[c]==False:
            revDfs(c,visited)

def addEdges(u,v):
    graph[u].append(v) 
def main():
    n,m=map(int,input().split())
    for i in range(1,n+1):
        graph[i]=[]
    for _ in range(m):
        u,v=map(int,input().split())
        addEdges(u,v)
    print(graph)
    visited=[False]*(n+1)
    dfs(1,visited)
    print()
    
    #step1:
    st=[]
    visited=[False]*(n+1)
    for i in range(1,n+1):
        if visited[i]==False:
            sort_graph(i,visited,st)
    print(st)
    #step 2:
    transpose_graph()
    
    #step 3:
    visited=[False]*(n+1)
    scc=0
    for i in range(n):
        nd=st.pop()
        if visited[nd]==False:
            revDfs(nd,visited)
            print()
            scc+=1
    print("no of strongly connected components:",scc)

main()
