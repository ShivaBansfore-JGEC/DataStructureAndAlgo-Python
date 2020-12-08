import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

'''
    NO OF DIVISORS 
    TIME -- O(SQRT(N))

    algo:
    find power of its prime factors 
    let say 

    2^1 , 3^2 or 2^y1,3^y2
    then total divisors =(y1+1)*(y2+1)......(yn+k)
    ex:
    divisor of 18=(1+1)*(2+1)=6


'''

def divisor(n):
    i=2
    d=1
    while i*i<=n:
        if n%i==0:
            cnt=1 #it is started with 1 becouse latter we will have to increament by 1
            while n%i==0:
                n//=i 
                cnt+=1
            d*=cnt
        i+=1
    if n>1:
        d*=2
    print(d)
            
for _ in range(int(input())):
    n=int(input())
    divisor(n)