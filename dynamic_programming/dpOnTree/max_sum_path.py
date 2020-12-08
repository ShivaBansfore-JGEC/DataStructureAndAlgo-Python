import sys
sys.stdout = open('dynamic_programming/dpOnTree/output.txt', 'w')
sys.stdin = open('dynamic_programming/dpOnTree/input.txt', 'r')
graph={}
for i in range(1,15):
    graph[i]=[]
dp=[0]*100

def dfs(a,g,u,parent):
    dp[u]=a[u-1]

    mx=0
    for child in g[u]:
        if child==parent:
            continue 
        dfs(a,g,child,u)

        mx=max(mx,dp[child])
    dp[u]+=mx

        



for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    for _ in range(n-1):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    dfs(a,graph,1,0)
print(dp[1])