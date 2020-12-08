import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')


#RECURSIVE SOLUTION
max_size=float('inf')
def coinChange(coins,amount,n):
    if amount==0:
        return 0
    ans=float("inf")
    for i in range(n):
        if amount-coins[i]>=0:
            smallAns=coinChange(coins,amount-coins[i],n)
            if smallAns!=max_size:
                ans=min(ans,smallAns+1)
    return ans 


#Top DOWN DP
def coinChangeTopDown(coins,amount,n,dp):
    if amount==0:
        return 0
    
    if dp[amount]!=max_size:
        return dp[n]

    ans=float('inf')
    for i in range(n):
        if amount-coins[i]>=0:
            small=coinChangeTopDown(coins,amount-coins[i],n,dp)
            if small!=max_size:
                ans=min(ans,small+1)
    dp[amount]=ans
    return ans

#Bottom Up 

def minCoinChange(coins,n,amount):
    dp=[max_size]*(amount+1)

    dp[0]=0

    for rupay in range(1,amount+1):
        for  i in range(n):
            if coins[i]<=rupay:
                smallAns=dp[rupay-coins[i]]
                if smallAns!=max_size:
                    dp[rupay]=min(dp[rupay],smallAns+1)
    return dp[amount]




n=int(input())
coins=list(map(int,input().split()))
amount=int(input())
print(coinChange(coins,amount,n))
dp=[max_size]*(amount+1)
print(coinChangeTopDown(coins,amount,n,dp))
print(minCoinChange(coins,n,amount))
