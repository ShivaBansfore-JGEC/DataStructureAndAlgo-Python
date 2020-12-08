import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')
mod=100000007
arr=[None]*3
def mul(A,B,dim):
    res=[[0 for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                x=(A[i][k]*B[k][j])%mod
                res[i][j]=(res[i][j]+x)%mod
    
    for i in range(dim):
        for j in range(dim):
            A[i][j]=res[i][j]

def printM(a,dim):
    for i in range(dim):
        for j in range(dim):
            print(a[i][j],end=" ")
        print()

def getfib(n):
    I=[[None for i in range(3)] for j in range(3)]
    T=[[None for i in range(3)] for j in range(3)]
    if n<=2:return arr[n]

    I[1][1]=I[2][2]=1
    I[1][2]=I[2][1]=0

    T[1][1]=0
    T[1][2]=T[2][1]=T[2][2]=1

    n=n-1
    while n:
        if n%2!=0:
            mul(I,T,2)
            n-=1
        else:
            mul(T,T,2)
            n//=2
    fn=(arr[1]*I[1][1]+arr[2]*I[2][1])%mod 
    return fn 





for _ in range(int(input())):
    f1,f2,n=map(int,input().split())
    arr[1]=f1 
    arr[2]=f2 
    n+=1
    print(getfib(n))

    