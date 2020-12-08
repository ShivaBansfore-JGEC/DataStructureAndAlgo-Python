import sys
sys.stdout = open('combinatorics/output.txt', 'w')
sys.stdin = open('combinatorics/input.txt', 'r')

# top down solution 
def ncr(n,k,dp):
    if dp[n][k]!=-1:
        return dp[n][k]

    if k==0 or k==n:
        return 1 
    dp[n][k]=ncr(n-1,k-1,dp)+ncr(n-1,k,dp)
    return dp[n][k]


#bottom up 
def binomialcoefficient(n,k):
    dp=[[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                dp[i][j]=1 
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

    return dp[n][k]

# space optimezed 
def binomial(n,k):
    dp=[0 for i in range(k+1)]
    dp[0]=1
    for i in range(1,n+1):
        j=min(i,k) 
        while j>0:
            dp[j]=(dp[j]+dp[j-1])%13
            j-=1
    print(dp)
    return dp[k]




n,k=map(int,input().split())
dp=[[-1 for i in range(k+1)] for j in range(n+1)]
print(ncr(n,k,dp))
print(binomialcoefficient(n,k))
print(binomial(n,k))