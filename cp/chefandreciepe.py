import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r') 
'''
for _ in range(int(input())):
    w=list(map(int,input().split()))
    n=len(w)
    p=w[n-1]
    week=24*5
    total=(sum(w)-p)*p
    if total>week:
        print("Yes")
    else:
        print("No")
'''
'''
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d=0
    sum1=0
    sum2=0
    for i in range(n):
      if sum1==sum2 and a[i]==b[i]:
        d+=a[i]
      sum1+=a[i]
      sum2+=b[i]
    print(d)

'''
'''
from collections import defaultdict 

graph = defaultdict(list) 

def addEdges(u,v):
    graph[u].append(v)

def find_all_paths(graph, start, end, path =[]): 
  path = path + [start] 
  if start == end: 
    return [path] 
  paths = [] 
  for node in graph[start]: 
    if node not in path: 
      newpaths = find_all_paths(graph, node, end, path) 
    for newpath in newpaths: 
      paths.append(newpath) 
  return paths 

for _ in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    for _ in range(n-1):
        u,v=map(int,input().split())
        addEdges(u,v)
    for _ in range(q):
        a,b=map(int,input().split())

  '''
  #CONVERT THE STRING
for _ in range(int(input())):
  n=int(input())
  a=input()
  b=input()
    
  for i in range(n):
    if b[i] not in a:
      print(-1)
      break
  for i in range(n):
    if a[i]<b[i]:
      print(-1)
      break
        
