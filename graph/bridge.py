import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')

'''
input:
4 4
1 2
2 3
2 4
3 4

'''


n,e=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(e):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
timer=0
enter=[0]*(n+1)
low=[0]*(n+1)

def dfs(graph,u,par,n,visited):
    global timer
    global enter 
    global low 
    visited[u]=True 
    enter[u]=low[u]=timer
    timer+=1
    for child in graph[u]:
        if child==par:continue
        
        if visited[child]:
            #there is back edgge
            print(u,child)
            low[u]=min(low[u],enter[child])
        else:
            dfs(graph,child,u,n,visited)
            if low[child]>enter[u]:
                print(u,"-->",child,"is a bridge")
            low[u]=min(low[u],low[child])

visited=[False]*(n+1)
dfs(graph,1,-1,n,visited)
#print(graph)
