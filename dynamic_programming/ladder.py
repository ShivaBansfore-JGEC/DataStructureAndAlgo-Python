import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

#RECURSIVE SOLUTION 
def ladder(n,k):
    if n==0:
        return 1
    count=0
    for i in range(1,k+1):
        if n-i>=0:
            count=count+ladder(n-i,k)
    return count 

#TOP DOWN DP
def LaddertopDOwnDp(n,k,dp):
    if n==0:
        return 1 
    
    if dp[n]!=-1:
        return dp[n]

    count=0
    for i in range(1,k+1):
        if n-i>=0:
            count=count+LaddertopDOwnDp(n-i,k,dp) 

    dp[n]=count
    return dp[n]


def LadderBottomUp(n,k):
    dp=[0]*(n+1)
    dp[0]=1

    for i in range(n+1):
        for j in range(1,k+1):
            if i-j>=0:
                dp[i]+=dp[i-j]
    return dp[n]


n=int(input())
k=int(input())
print(ladder(n,k))
dp=[-1]*(n+1)
print(LaddertopDOwnDp(n,k,dp))
print(LadderBottomUp(n,k))
