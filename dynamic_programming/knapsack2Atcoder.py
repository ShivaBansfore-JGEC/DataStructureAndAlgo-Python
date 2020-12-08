import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')
inf=10**10
def knapsackBottomUp(wt,price,c,n,m):
    dp=[[inf for x in range(m+1)] for y in range(n+1)]
    for l in range(n+1):
        dp[l][0]=0


    for i in range(1,n+1):
        wi=wt[i];vi=price[i]
        for V in range(1,m+1):
            if vi <= V:
                dp[i][V]=min(wi+dp[i-1][V-vi],dp[i-1][V])
            else:
                dp[i][V]=dp[i-1][V]

    res=0
    for i in range(m+1):
        if dp[n][i]<=c:
            res=i
    print(res)
n,c=map(int,input().split())
wt=[]
price=[]
wt.append(0)
price.append(0)
for _ in range(n):
    w,v=map(int,input().split())
    wt.append(w)
    price.append(v)
max_val=sum(price)
knapsackBottomUp(wt,price,c,n,max_val)