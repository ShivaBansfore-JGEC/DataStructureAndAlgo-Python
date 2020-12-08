import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')
def primeSieve(n):
    sieve=[1]*1000
    sieve[0]=sieve[1]=0
    i=2
    while i*i<=n:
        if sieve[i]==1:
            j=i*i 
            while j<=n:
                sieve[j]=0
                j+=i #adding i to get next multipl i
        i+=1
    for k in range(2,n):
        if sieve[k]==1:
            print(k,end=" ")

n=int(input())
primeSieve(n)