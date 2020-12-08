import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

N=int(input())
dp=[0]*3
flag=0
for _ in range(N):
    a=list(map(int,input().split()))
    if flag==0:
        dp[0]=a[0]
        dp[1]=a[1]
        dp[2]=a[2]
        flag=1
    else:
        a0=dp[0]
        a1=dp[1]
        a2=dp[2]
        dp[0]=max(a[0]+a1,a[0]+a2)
        dp[1]=max(a[1]+a0,a[1]+a2)
        dp[2]=max(a[2]+a0,a[2]+a1)
print(max(dp))