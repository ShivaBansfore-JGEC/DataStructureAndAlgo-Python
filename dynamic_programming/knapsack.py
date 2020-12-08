import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

#RECURSIVE APPROACH
def knapsack(wt,price,c,n):
    if n==0:
        return 0
    
    inc=exc=0

    if wt[n-1]<=c:
        inc=price[n-1]+knapsack(wt,price,c-wt[n-1],n-1)
    
    exc=knapsack(wt,price,c,n-1)

    return max(inc,exc)

#TOP DOWN 
def knapsackTopDown(wt,price,c,n,dp):
    if n==0 or c==0:
        return 0
    if dp[n-1]>=0:
        return dp[n-1]
    inc=exc=0
    if wt[n-1]<=c:
        inc=price[n-1]+knapsackTopDown(wt,price,c-wt[n-1],n,dp)
    
    exc=knapsackTopDown(wt,price,c,n-1,dp)
    dp[n-1]=max(inc,exc)
    return dp[n-1]


#BottomUp

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
    
    print(dp)
    return dp[n][c]



wt=list(map(int,input().split()))
price=list(map(int,input().split()))
c=int(input())
print(knapsack(wt,price,c,len(wt)))
dp=[-1]*(len(wt))
print(knapsackTopDown(wt,price,c,len(wt),dp))
print(dp)
print(knapsackBottomUp(wt,price,c,len(wt)))