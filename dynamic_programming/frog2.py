import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')
def printD(dp,k,n):
    for i in range(n):
        for j in range(k+1):
            print(dp[i][j],end=" ")
        print()
def frog2(N,h,k):
    dp=[sys.maxsize-1]*N
    dp[0]=0
    for i in range(N):
        for j in range(i+1,i+k+1):
            if j<N:
                dp[j]=min(dp[j],dp[i]+abs(h[i]-h[j]))
    return dp[N-1]

N,k=map(int,input().split())
h=list(map(int,input().split()))
print(frog2(N,h,k))
