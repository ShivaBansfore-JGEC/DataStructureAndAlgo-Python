import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')


prm=[]

def SieveOfEratosthenes(n): 
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

for i in range(int(input())):
    n=int(input())
    SieveOfEratosthenes(n)
    sum=0
    l=[]
    m=len(prm)
    for i in range(m):
        for j in range(i+1,m):
            if(sum+(prm[i]*prm[j])<=n):
                sum+=(prm[i]*prm[j]);
                l.append(prm[i]*prm[j])
    
    if(len(l)<3):
        print("NO")
    else:
        if(len(l)==4):
            print("YES")
            print(*l)
        else:
            print("YES")
            l.append(n-sum)
            print(*l)
    prm.clear()
    l.clear()


        