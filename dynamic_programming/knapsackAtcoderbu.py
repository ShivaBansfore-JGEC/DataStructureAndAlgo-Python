import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

def knapsackBottomUp(wt,price,c,n):
    dp=[[0 for x in range(c+1)] for y in range(n+1)]
    for i in range(n+1):
        for w in range(c+1):
            if i==0 or w==0:
                dp[i][w]=0
            else:
                inc=exc=0
                if wt[i-1]<=w:
                    inc=price[i-1]+dp[i-1][w-wt[i-1]]
                exc=dp[i-1][w]
                dp[i][w]=max(inc,exc)

    
    return dp[n][c]





n,c=map(int,input().split())
wt=[]
price=[]
for _ in range(n):
    w,v=map(int,input().split())
    wt.append(w)
    price.append(v)
print(knapsackBottomUp(wt,price,c,n))