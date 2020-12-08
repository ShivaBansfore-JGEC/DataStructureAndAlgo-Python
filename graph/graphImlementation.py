import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')
# n vertices and m edges
graph={}
def addEdges(u,v):
    graph[u].append(v)
    graph[v].append(u)

#BFS
def bfs(src):
    q=[]
    visited=[False]*100
    q.append(src)

    while q:
        v=q.pop(0)
        visited[v]=True 
        print(v,end=" ")

        for nbr in graph[v]:
            if visited[nbr]==False:
                q.append(nbr)
                visited[nbr]=True

# dfs Recursive
def dfs(u,parent,visited):
    visited[u]=True
    #print(u,end=" ")
    for child in graph[u]:
        if visited[child]==False:
            dfs(child,u,visited)
def dfs1(u,parent,visited):
    visited[u]=True
    for child in graph[u]:
        if visited[child]==False:
            dfs(child,u,visited)

#dfs iterative using stack
def dfsUsingStack(u):
    stack=[]
    stack.append(u)
    visited=[False]*100
    visited[u]=True
    while stack:
        r=stack.pop()
        #if visited[r]==True:
            #continue 
        #visited[r]=True 
        print(r,end=" ")

        for c in graph[r]:
            if visited[c]==False:
                stack.append(c)
                visited[c]=True

def detectCycle(u):
    q=[]
    visited=[False]*100
    q.append(u)

    while q:
        v=q.pop(0)
        if visited[v]==True:
            return True 

        visited[v]=True 

        for nbr in graph[v]:
            if visited[nbr]==False:
                q.append(nbr)

    return False 

def isConnected(u,n):
    stack=[]
    stack.append(u)
    visited=[False]*100
    visited[u]=True
    while stack:
        r=stack.pop()
        #if visited[r]==True:
            #continue 
        #visited[r]=True 
        #print(r,end=" ")

        for c in graph[r]:
            if visited[c]==False:
                stack.append(c)
                visited[c]=True
    for i in range(n):
        if visited[i]==False:
            return False 
    return True 

        
def main():
    n,m=map(int,input().split())
    for i in range(n):
        graph[i]=[]

    for _ in range(m):
        u,v=map(int,input().split())
        addEdges(u,v)
    bfs(0)
    print()
    visited=[False]*100
    dfs(0,0,visited)
    print()
    dfsUsingStack(0)
    print()
    print(graph)
    print(detectCycle(0))
    print(isConnected(0,n))

    #numbet of connected components
    c=0
    visited=[False]*100
    for i in range(n):
        if visited[i]==False:
            dfs1(i,i,visited)
            c+=1
    print("no of connected components:",c)


main()