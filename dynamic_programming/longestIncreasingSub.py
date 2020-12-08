import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

def LongestIncreasingSub(a,n):
    dp=[0]*n
    dp[0]=1

    for i in range(1,n):
        dp[i]=1
        for j in range(i-1,0,-1):
            if a[j]>a[i]:
                continue
            posAns=dp[j]+1
            if posAns>dp[i]:
                dp[i]=posAns 
    best=0
    for i in range(n):
        if best<dp[i]:
            best=dp[i]
    return best 

            

n=int(input())
a=list(map(int,input().split()))
print(LongestIncreasingSub(a,n))