import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

def primeFactorization(n):
    i=2
    while i*i<=n:
        if n%i==0:
            cnt=0
            while n%i==0:
                cnt+=1
                n//=i 
            print(str(i)+"^"+str(cnt))
        i+=1
    if n>1:
        print(str(n)+"^"+"1")


n=int(input())
primeFactorization(n)
