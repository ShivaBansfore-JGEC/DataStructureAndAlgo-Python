import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

'''
    SUM OF DIVISORS 
    TIME SQRT(N)*LOG(N)

    algo:
    find the prime factors of number 
    and apply the sum of series formula
    s(n)=(p1^e1+1//p1-1)*(p2^e2+1//p2-1)......pn^en+1//pn-1
'''
def power(a,n):
    res=1
    while n:
        if n%2!=0:
            res*=a 
            n-=1
        else:
            a=(a*a)
            n//=2
    return res 

def sumOfDivisors(n):
    total=1
    i=2
    while i*i<=n:
        if n%i==0:
            cnt=1
            while n%i==0:
                n//=i 
                cnt+=1
            total*=((power(i,cnt)-1)//(i-1))
        i+=1

    if n>1:
        total*=((power(n,2)-1)//(n-1))
    return total 

            




for _ in range(int(input())):
    n=int(input())
    