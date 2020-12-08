import sys
sys.stdout = open('combinatorics/output.txt', 'w')
sys.stdin = open('combinatorics/input.txt', 'r')

def ncr(n,k,p):
    dp=[0 for i in range(k+1)]
    dp[0]=1
    
    for i in range(n+1):
        j=min(i,k)
        while j>0:
            dp[j]=(dp[j]+dp[j-1])%p
            j-=1
    return dp[k]
def lucas(n,r,p):
    if r==0:
        return 1 
    
    ni=int(n%p)
    ri=int(r%p)
    return (lucas(n//p,r//p,p)*ncr(ni,ri,p))



for _ in range(int(input())):
    n,k,p=map(int,input().split())
    print(lucas(n,k,p))
