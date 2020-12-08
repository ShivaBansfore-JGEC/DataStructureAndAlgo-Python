import sys
sys.setrecursionlimit(10**9)
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

graph={}
n,m=map(int,input().split())
for i in range(1,n+1):
    graph[i]=[]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)

def dfs(i,dp):
    temp=0
    if dp[i]!=-1:
        return dp[i]
    for nvr in graph[i]:
        temp=max(temp,dfs(nvr,dp)+1)
    dp[i]=temp
    return temp 

dp=[-1]*(n+1)
res=0
for i in range(1,n+1):
    res=max(res,dfs(i,dp))
print(res)
#print(graph)