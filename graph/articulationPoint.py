import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[False]*(n+1)
I=[-1]*(n+1)
low=[-1]*(n+1)
timer=1
#children=0
def isCutpoint(u):
    print(v)

def dfs(u,p=-1):
    global timer
    global visited
    global I 
    global low
    #global children
    visited[u]=True 
    I[u]=low[u]=timer
    timer+=1
    children=0
    for child in graph[u]:
        if child==p:
            continue 

        if visited[child]:
            low[u]=min(low[u],I[child])
        else:
            dfs(child,u)
            low[u]=min(low[u],low[child])
            if low[child]>=I[u] and p!=-1:
                isCutpoint(u)
            children+=1
    if p==-1 and children>1:
        isCutpoint(u)
    #print(I)
    #print(low)

print(graph)
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
