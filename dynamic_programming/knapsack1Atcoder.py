import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

def knapsack(wt,price,n,c,dp):
    if n<0 or c==0:
        return 0
    if dp[n][c]!=-1:
        return dp[n][c]
    inc=exc=0
    if c>=wt[n]:
        inc=price[n]+knapsack(wt,price,n-1,c-wt[n],dp)
    exc=0+knapsack(wt,price,n-1,c,dp)
    dp[n][c]=max(inc,exc)
    return max(inc,exc)

n,c=map(int,input().split())
wt=[]
price=[]
for _ in range(n):
    w,v=map(int,input().split())
    wt.append(w)
    price.append(v)
dp=[[-1 for x in range(c+1)] for y in range(n+1)]
print(knapsack(wt,price,n-1,c,dp))