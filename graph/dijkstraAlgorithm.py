import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')

'''
  Algo:
    1.represent graph using matrix and take wt array ,parent and visited 
    array and assign wt[0]=0 assign the rest of wt inf

    2. run a loop through all vertices and find the minimum
    vetex with min wt and mark it as visited

    3. find all the neighbour and compare its orginal value with
       distance and assign (wt of source + wt of dst)


    input:

    5 7
    0 1 4
    0 2 8
    1 3 5
    1 2 2
    2 3 5
    2 4 9
    3 4 4

'''

def findMinVertex(distance,visited,n):
    minVertex=-1
    for i in range(n):
        if not visited[i] and (minVertex==-1 or distance[i]<distance[minVertex]):
            minVertex=i
    return minVertex 

def dijkstra(graph,n):
    distance=[sys.maxsize-1]*n 
    visited=[False]*n
    distance[0]=0

    for _ in range(n-1):
        minVertex=findMinVertex(distance,visited,n)
        visited[minVertex]=True
        for j in range(n):
            if graph[minVertex][j]!=0 and not visited[j]:
                dist=distance[minVertex]+graph[minVertex][j]
                if dist<distance[j]:
                    distance[j]=dist
    
    for i in range(n):
        print(i,":",distance[i])






n,e=map(int,input().split())
graph=[[0 for i in range(n) ] for j in range(n)]
for _ in range(e):
    f,s,w=map(int,input().split())
    graph[f][s]=w 
    graph[s][f]=w
dijkstra(graph,n)