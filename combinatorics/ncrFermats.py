import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

def  power(a,n,p):
    res =1 
    while n:
        if n%2!=0:
            res=(res*a)%p 
            n-=1
        a=(a*a)%p 
        n//=2 
    return res 
def molduloInverse(n,p):
    return power(n,p-2,p)

def ncrUsingFermat(n,r,p):
    if r==0:
        return 1 
    fact=[0]*(n+1)
    fact[0]=1 
    for i in range(1,n+1):
        fact[i]=(fact[i-1]*i)%p
    
    return (fact[n]*(molduloInverse(fact[r],p)%p)*molduloInverse(fact[n-r],p)%p)%p


for _ in range(int(input())):
    n,r,p=map(int,input().split())
    '''
        fact[n]*inv[r]*inv[n-r]

    '''
    print(ncrUsingFermat(n,r,p))