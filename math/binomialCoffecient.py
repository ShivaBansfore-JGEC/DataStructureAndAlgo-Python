import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')
p=1000000007
f=[0]*1000001

def power(a,n):
    res=1
    while n:
        if n%2!=0:
            res=(res*a)%p 
            n-=1
        else:
            a=(a*a)%p 
            n//=2
    return res 

def c(n,k):

    res=f[n]%p 
    res=((res%p)*(power(f[k],p-2)%p))%p
    res=((res%p)*(power(f[n-k],p-2)%p))%p

    return res




f[0]=f[1]=1
for i in range(2,1000001):
    f[i]=((f[i-1]%p)*i%p)%p 

for _ in range(int(input())):
    n,k=map(int,input().split())
    print(c(n,k))