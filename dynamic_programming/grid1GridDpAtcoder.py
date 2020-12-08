import sys
sys.setrecursionlimit(10**9)
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')
mod=1000000007
h,w=map(int,input().split())
grid=[]
for _ in range(h):
    s=list(input())
    grid.append(s)

dp=[[0 for i in range(w)] for j in range(h)]
dp[0][0]=1
for i in range(h):
    for j in range(w):
        if grid[i][j]=='#':
            continue
        if i>0:
            dp[i][j]+=dp[i-1][j]%mod
        
        if j>0:
            dp[i][j]+=dp[i][j-1]%mod
        
print(dp[h-1][w-1]%mod)