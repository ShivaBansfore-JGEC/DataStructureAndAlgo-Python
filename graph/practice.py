import sys
import math
from collections import defaultdict
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
parent=[-1]*(n+1)
level=[0]*(n+1)
maxN=int(math.log2(n))
sparseTable=[[-1 for i in range(maxN+1)] for j in range(n+1)]
def printM(table):
    for i in range(n+1):
        for j in range(maxN+1):
            print(table[i][j],end=" ")
        print()

        
def bfs(u):
    q=[]
    visited=[False]*(n+1)
    level[u]=0
    q.append(u)
    while q:
        x=q.pop(0)
        visited[x]=True
        for c in graph[x]:
            if visited[c]==False:
                q.append(c)
                level[c]=level[x]+1
                visited[c]=True 

def dfs(u,p=-1):
    global parent
    parent[u]=p
    sparseTable[u][0]=p 
    for c in graph[u]:
        if c==p:
            continue
        dfs(c,u)

def lca(a,b,root):
    visited=[False]*(n+1)
    lca=-1
    while True:
        visited[a]=True
        if a==root:
            break 
        a=parent[a]
    
    while True:
        if visited[b]==True:
            lca=b 
            break  
        b=parent[b]
    return lca        
def init():
    
    for i in range(1,maxN+1):
        for j in range(1,n+1):
            if sparseTable[j][i-1]!=-1:
                par=sparseTable[j][i-1]
                sparseTable[j][i]=sparseTable[par][i-1]



def binaryLifting(a,b):
    if level[a]>level[b]:
        a,b=b,a 
    d=level[b]-level[a]
    while d>0:
        i=int(math.log2(d))
        print("i-->",i)
        b=sparseTable[b][i]
        d-=(1<<i)
    
    if a==b: return a 

    for i in range(maxN,-1,-1):
        if sparseTable[a][i]!=-1 and sparseTable[a][i]!=sparseTable[b][i]:
            a=sparseTable[a][i]
            b=sparseTable[b][i]
    return sparseTable[a][0]



#STONGLY CONNECTED COMPONENT
#KOSARAJU'S ALGORITHM

# step1:SORTING THE GRAPH
visited=[False]*(n+1) 
def sort(u,st,p=-1):
    global visited
    visited[u]=True 
    for c in graph[u]:
        if c==p:
            continue 
        sort(c,st,u)
    st.append(u)
tg=defaultdict(list)

#step 2:transposing graph 
for i in range(1,n+1):
    for j in graph[i]:
        tg[j].append(i)

#step3: rev dfs 
def revDfs(u,visited,p=-1):
    visited[u]=True
    print(u,end=" ")
    for c in tg[u]:
        if visited[c]==False:
            revDfs(c,visited,u)



#main()

print(graph)
dfs(1)
print(parent)
bfs(1)
#print(level)
init()
print(lca(6,4,1))
printM(sparseTable)
print(1<<3)
print(binaryLifting(5,4))
st=[]
for i in range(1,n+1):
    if not visited[i]:
        sort(i,st)
print(st)

visited=[False]*(n+1)
scc=0
for _ in range(n):
    nd=st.pop()
    if not visited[nd]:
        revDfs(nd,visited)
        print()
        scc+=1
print(scc)
