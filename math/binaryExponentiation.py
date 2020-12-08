import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

def power(base,n):
    res=1
    while n:
        if n%2!=0:
            res=res*base
            n-=1
        else:
            base*=base 
            n//=2
    return res 
n,m=map(int,input().split())
print(power(n,m))