import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

def frog1(N,h):
    dp=[0]*(N+1)
    dp[0]=0
    dp[1]=abs(h[1]-h[0])

    for i in range(2,N):
        dp[i]=min((abs(h[i]-h[i-1])+dp[i-1]),(abs(h[i]-h[i-2])+dp[i-2]))

    return dp[N-1]


N=int(input())
h=list(map(int,input().split()))
print(frog1(N,h))