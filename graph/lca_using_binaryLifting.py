import sys
import math
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')

'''
Algo:
step1:prepare graph and find the level of each node 

step2:prepare sparse table of size n x log2(n) and fill the oth column by using dfs

step3:fill the entire sparse table using dynammic programming 

step4: write a fuction of lca with binary lifting ,find distance between two node 
      and take a jump in power of 2 

time complexity: O(nlog(n)) for precompution and query(O(log(n))) 
space complexity is O(nlog(n))

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

def printM(lca,m,n):
    for i in range(n):
        for j in range(m):
            print(lca[i][j],end=" ")
        print()

n,m=map(int,input().split())
parent=[sys.maxsize-1]*(n+1)
level=[0]*(n+1)
parent[0]=-1
graph=[[] for i in range(n+1)]

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

maxN=int(math.log2(n))
lca=[[-1 for i in range(maxN+1)] for j in range(n+1)]

#bfs
#step 1: find out level of of each node 
def bfs(src):
    q=[]
    visited=[False]*(n+1)
    q.append(src)
    level[src]=0
    visited[src]=True
    while q:
        x=q.pop(0)
        for i in graph[x]:
            if visited[i]==False:
                q.append(i)
                level[i]=level[x]+1
                visited[i]=True

# dfs 
#step 2: prepare sparse table using dfs 

def dfs(u,p):
    lca[u][0]=p 
    for child in graph[u]:
        if child==p:
            continue 
        dfs(child,u)

def initTable():
    for i in range(1,maxN+1):
        for j in range(n+1):
            if lca[j][i-1]!=-1:
                par=lca[j][i-1]
                lca[j][i]=lca[par][i-1]

    
#step 4: lca using binary lifting 
def Lca(a,b):
    if level[a]>level[b]:
        a,b=b,a
    # finding distance between level of two node 
    d=level[b]-level[a]

    while d>0:
        #now we will make jump in power of 2 binary lifiting 
        i=int(math.log2(d))
        b=lca[b][i]
        d-=(1<<i)
    if a==b:return a 
    #now we have reached to the same level and its time to move together towords
    #common ancestor
    #if we make a jump linearly it will increase time complexity
    #we we will jump directly 2**max
    for i in range(maxN,-1,-1):
        if lca[a][i]!=-1 and lca[a][i]!=lca[b][i]:#checking if they are nor leading their ancestor
            a=lca[a][i]
            b=lca[b][i]

    return lca[a][0]




#print(graph)
bfs(0)
dfs(0,-1)
initTable()
#print(level)
#printM(lca,maxN+1,n+1)
print(graph)
print(Lca(6,4))