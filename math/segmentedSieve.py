import sys
import math 
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

prm=[]

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            prm.append(p)

def segmentedSieve(l,r,prime):
    if l==1:l+=1
    maxN=r-l+1
    sieve=[0]*maxN 

    for p in prime:
        if p*p<=r:
            i=(l//p)*p
            if i < l:i+=p

            while i<=r:
                if i!=p:
                    sieve[i-l]=1
                i+=p 
    for i in range(maxN):
        if sieve[i]==0:
            print(l+i,end=" ")




n=int(input())
l,r=map(int,input().split())
maxN=int(math.sqrt(r))
primeSieve(n)
i=2 
segmentedSieve(l,r,prime)