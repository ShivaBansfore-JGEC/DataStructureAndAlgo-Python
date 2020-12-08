import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

#TOP DOWN APPROACH
def fib(n,dp):
    if n==0 or n==1:
        return n 
    
    if dp[n]!=-1:
        return dp[n]
    
    dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]



#BOTTOM UP APROACH 

def fibBottoUp(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]

    #time o(n)
    #space o(n)


def fibBottoUp1(n):
    a=0
    b=1
    z=0
    
    for _ in range(2,n+1):
        z=(a+b)
        a=b
        b=z

    print(z)
#time o(n)
#space o(1)




n=int(input())
dp=[-1]*(n+1)
print(fib(n,dp))
print(fibBottoUp(n))
fibBottoUp1(n)
