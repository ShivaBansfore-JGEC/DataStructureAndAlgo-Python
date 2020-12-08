import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')
'''
input:
1
3
'''
#USING A BINOMIAL COEFFICIENT 
# ncr using dp

def ncrDp(n,k):
    dp=[0 for i in range(k+1)]
    dp[0]=1 
    
    for i in range(1,n+1):
        j=min(i,k)

        while j>0:
            dp[j]=(dp[j]+dp[j-1])
            j-=1

    return dp[k]



#USING BOTOOM UP DP 
def catalanNumber(k):
    dp=[0]*(k+1)
    dp[0]=dp[1]=1
    for i in range(2,k+1):
        for j in range(i):
            dp[i]+=(dp[j]*dp[i-j-1])
    print(dp)
    return dp[k]

for _ in range(int(input())):
    n=int(input())
    print(catalanNumber(n))
    c=ncrDp(2*n,n)
    print(c//(n+1))

