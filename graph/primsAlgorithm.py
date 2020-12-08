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
       wt assing the minimum val at wt array
       minVertex will be parent of current vertes 
       finally print output graph or mst 


'''




def findMinVertex(weight,visited,n):
    minVer=-1
    for i in range(n):
        if not visited[i] and (minVer==-1 or weight[i]<weight[minVer]):
            minVer=i
    return minVer
def primes(graph,n):
    parent=[None]*n
    weight=[sys.maxsize-1]*n 
    visited=[False]*n 
    weight[0]=0
    parent[0]=-1

    for _ in range(n):
        #find min vertex
        minVertex=findMinVertex(weight,visited,n)
        visited[minVertex]=True
        #explore all the nbr vertex
        for j in range(n):
            if graph[minVertex][j]!=0 and not visited[j]:
                if graph[minVertex][j]<weight[j]:
                    weight[j]=graph[minVertex][j]
                    parent[j]=minVertex
    print(weight)
    print(parent)
    for i in range(1,n):
        if parent[i]<i:
            print(parent[i]," ",i," ",weight[i]) 
        else:
            print(i," ",parent[i]," ",weight[i])


n,e=map(int,input().split())
graph=[[0 for i in range(n) ] for j in range(n)]
for _ in range(e):
    f,s,w=map(int,input().split())
    graph[f][s]=w 
    graph[s][f]=w 
primes(graph,n)