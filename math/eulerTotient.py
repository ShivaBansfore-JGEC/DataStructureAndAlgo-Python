import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

ph=[0]*1000001

def phii(n):

    for i in range(1,1000001):
        ph[i]=i 
    
    for i in range(2,n+1):
            ph[i]

            for j in range(i,n+1,i):    
                ph[j]//=i
                ph[j]*=(i-1)
    

def phi(n):
    res=n 
    i=2 
    while i*i<=n:
        if n%i==0:
            res//=i 
            res*=(i-1)
        while n%i==0:
            n//=i 
        i+=1
    if n>1:
        res//=n
        res*=(n-1)

    return res 


for _ in range(int(input())):
    n=int(input())
    print(phi(n))
    #phii(1000000)
    #print(ph[n])