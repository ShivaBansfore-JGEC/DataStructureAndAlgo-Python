import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')

#PROBLEM A
'''
for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%2==0:
        print(n+(2*k))
    else:
        f=0
        d=2
        while d < n//2:
            if n%d==0:
                f=1
                break
            d+=1
        if f==0:
            d=n
        
        print((n+d)+(2*(k-1)))
'''
def models(a,id,n):
    if id>n:
        return 0

    count=0
    i=id 
    while i < (n+1):
        if a[i]>a[id]:
            count=max(count,1+models(a,i,n))
        i+=id
    return count
for _ in range(int(input())):

    n=int(input())
    a=list(map(int,input().split()))
    maxi=1
    for i in range(n):
        maxi=max(maxi,1+models(a,i,n))
    print(maxi)

'''
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

a,b=map(int,input().split())
print(gcd(a,b))
'''