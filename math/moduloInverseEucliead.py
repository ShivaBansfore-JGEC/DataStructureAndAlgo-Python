import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

'''
   Modulo inverse using euclidean algo:

   There are to technique to find inverse modulo
   1.exteded euclidean algorithm 
   2.euler totient using fermats theorem 

'''
#1 USINF EXTENDED ALGOTITHM 

def exteded_eucliead(a,b):
    if b==0:
        return a ,1,0
    d,x1,y1=exteded_eucliead(b,a%b)
    x=y1 
    y=x1-y1*(a//b)
    return d,x,y

#2.USING FERMATS THEOREM 


def power(a,n,m):
    res=1
    while n:
        if n%2!=0:
            res=(res*a)%m 
            n-=1
        a=(a*a)%m
        n//=2
    return res%m


for _ in range(int(input())):
    a,b=map(int,input().split())
    v=exteded_eucliead(a,b)
    g=v[0]
    x=v[1]
    y=v[2]
    if g!=1:
        print("No Solution ")
    else:
        x=(x%b+b)%b 
        print(x)
    
    ans=power(a,b-2,b)
    print(ans)
