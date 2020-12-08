import sys
import math
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

def sumofdigit(n):
    s=str(n)
    for i in s:
        print(i)

for _ in range(int(input())):
    n=int(input())
    for _ in range(n):
        a,b=map(int,input().split())



   



        









'''
for _ in range(int(input())):
    n=int(input())
    if n%2!=0:
        print(n//2+1)
    else:
        print(n//2)
'''

























'''
def isPossible(a,t,k):
    for i in range(len(a)-(k-1)):
        s=0
        c=0
        for j in range(i,i+k,1):
            if s+a[j]<=t:
                s+=a[j]
                c+=1
        if c==k:
            return True 

    return False

def binarySearch(a,n,t):

    l=1
    r=n 
    ans=0
    while l<=r:
        mid=l+(r-l)//2
        if isPossible(a,t,mid):
            ans=mid 
            l=mid+1
        else:
            r=mid-1
    return ans 


n,t=map(int,input().split())
a=list(map(int,input().split()))
print(binarySearch(a,n,t))
#print(isPossible(a,t,3))
'''
'''
def binarySearch(k,a):
    ans=0 
    l=0
    r=len(a)-1
    while l<=r:
        mid=l+(r-l)//2 
        #print(a[mid])
        if a[mid]<=k:
            ans=mid+1
            l=mid+1
        else:
            if a[mid]<=k:
                ans+=1
            r=mid-1
    return ans 
n=int(input())
a=list(map(int,input().split()))
a.sort()
q=int(input())
for _ in range(q):
    val=int(input())
    print(binarySearch(val,a))
'''



'''
def is_Possible(n,k):
    s=0
    for i in range(1,n+1):
        s+=(i*5)
    if (s+k)<=240:
        return True 
    else:
        return False

def binarySearch(n,k):
    l=0
    r=n 
    ans=-1
    while l<=r:
        mid=l+(r-l)//2 
        if is_Possible(mid,k):
            ans=mid 
            l=mid+1 
        else:
            r=mid-1
    return ans


n,k=map(int,input().split())
print(binarySearch(n,k))

'''

'''
def divisors(n):
    #time complexity = sqrt(n)
    i=2 
    d=1
    while i*i<=n:
        if n%i==0:
            cnt=1
            while n%i==0:
                n//=i
                cnt+=1
            d*=cnt
        i+=1
    if n>1:
        d*=2
    if d==3:
        return True 
    else:
        return False

n=int(input())
a=list(map(int,input().split()))
for i in a:
    if divisors(i):
        print("YES")
    else:
        print("NO")

def noOfDivisors(n):
    i=1
    d=0
    while i*i<=n:
        if n%i==0:
            if i*i==n:
                d+=1
            else:
                d+=2
        i+=1
    if d==3:
        return True 
    else:
        return False

'''

'''
def isValid(a,n,d):
    pos=a[0]
    for i in range(1,n):
        if a[i]-pos>(2*d):
            return False 
        else:
            pos=a[i]
    return True 


def binarySearch(a,n,m):
    l=0
    ans=-1
    r=m-1
    while l<=r:
        mid=l+((r-l)*0.5)
        print(l,r,mid)
        if isValid(a,n,mid):
            #move left 
            ans=math.floor(mid)
    
            r=mid
        else:
            #move right
            l=mid
    return ans 




n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
print(binarySearch(a,n,l))


'''







'''
        COMBINATORICS
#SIMPLE RECURSSIVE SOLUTION 

def binomialRec(n,k):
    if k==0 or k==n:
        return 1 
    return binomialRec(n-1,k-1)+binomialRec(n-1,k)



#TOP DOWN DP SOLUTION 
def binomTopDp(n,k,dp):
    if dp[n][k]!=-1:
        return dp[n][k]
    if k==0 or k==n:
        return 1 
    dp[n][k]=binomTopDp(n-1,k-1,dp)+binomTopDp(n-1,k,dp)
    return dp[n][k]


#BOTTOM UP SOLUTION 
def binomialBottomUp(n,k):
    dp=[[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if j==0 or j==i:
                dp[i][j]=1 
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
    return dp[n][k]

#SPACE OPTIMIZED

def binom(n,k):
    dp=[0 for i in range(k+1)]
    dp[0]=1
    for i in range(n+1):
        j=min(i,k)
        while j>0:
            dp[j]=(dp[j]+dp[j-1])
            j-=1
    return dp[k]



for _ in range(int(input())):
    n,k=map(int,input().split())
    print(binomialRec(n,k))
    dp=[[-1 for i in range(k+1)] for j in range(n+1)]
    print(binomTopDp(n,k,dp))
    print(binomialBottomUp(n,k))
    print(binom(n,k))


'''

'''
a=[1]*100000
prime=[]
def sieve(n):
    a[0]=a[1]=0

    i=2 
    while i*i<=n:
        if a[i]==1:
            j=i*i 
            while j<=n:
                a[j]=0 
                j+=i 
        i+=1
    
    print(2,end=" ")
    prime.append(2)
    for i in range(3,n+1,2):
        if a[i]==1:
            print(i,end=" ")
            prime.append(i)

def segmentedSieve(l,r):
    if l==1:l+=1
    maxn=r-l+1
    sve=[0]*maxn
    for p in prime:
        if p*p<=r:
            i=(l//p)*p 
            if i < l:i+=p 
            while i<=r:
                if i!=p:
                    sve[i-l]=1 
                i+=p 

    for i in range(maxn):
        if sve[i]==0:
            print(l+i,end=" ")

for _ in range(int(input())):
    l,r=map(int,input().split())
    sieve(r)
    print()
    segmentedSieve(l,r)

'''


'''

#MATRIX EXPONENTIATION 

1
3 3
1 0 4
1 2 2
0 4






def mul(I,arr,dim):
    res=[[0 for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                res[i][j]+=I[i][k]*arr[k][j]
    
    for i in range(dim):
        for j in range(dim):
            I[i][j]=res[i][j]
            


def power(arr,dim,n):
    I=[[0 for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if i==j:
                I[i][j]=1 
    while n:
        if dim%2!=0:
            mul(I,arr,dim)
            n-=1
        else:
            mul(arr,arr,dim)
            n//=2 
    #coping all the value from identity matrix 

    for i in range(dim):
        for j in range(dim):
            arr[i][j]=I[i][j]


for _ in range(int(input())):
    n,dim=map(int,input().split())
    arr=[]
    for _ in range(dim):
        a=list(map(int,input().split()))
        arr.append(a)
    power(arr,dim,n)

    for i in range(dim):
        for j in range(dim):
            print(arr[i][j],end=" ")
        print()


'''



'''

def power(a,n):
    #time O(logn)
    res=1
    while n:
        if n%2!=0:
            res=res*a 
            n-=1
        else:
            a=(a*a)
            n//=2
    return res 



#number of divisors 
def divisors(n):
    #time complexity = sqrt(n)
    i=2 
    d=1
    while i*i<=n:
        if n%i==0:
            cnt=1
            while n%i==0:
                n//=i
                cnt+=1
            d=d*cnt
        i+=1
    if n>1:
        d*=2

def sumOfDivisors(n):
    #time sqrt(n)*logn
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

    print(total)
 
def D(n):
    dv=[]
    i=1
    while i*i<=n:
        if n%i==0:
            if i==n//i:
                dv.append(i)
            else:
                dv.append(i)
                dv.append(n//i)
        i+=1
    return dv

for _ in range(int(input())):
    n,m=map(int,input().split())
    d1=D(n)
    d2=D(m)
    if len(d1)<len(d2):
        c=0
        for i in d1:
            if i in d2:
                c+=1
        print(c)
    else:
        c=0
        for i in d2:
            if i in d1:
                c+=1
        print(c)

        

'''





























'''
def gcd(a,b):
    if b==0:
        return a 
    return gcd(b,a%b)

def isPerm(n,m):
    m=str(m)
    n=str(n)
    if len(m)!=len(n):
        return False 
    mp={}
    for i in m:
        if i in mp:
            mp[i]+=1
        else:
            mp[i]=1
    
    for i in n:
        if i in mp:
            continue 
        else:
            return False

    return True 




def euler(n):
    res=n 
    i=2 
    while i*i<=n:
        if n%i==0:
            res//=i 
            res*=(i-1)
        while n%i==0:
            n//=i
        i+=1
        
    if n>1:
        res*=(n-1)
        res//=n 
    return res 

for i in range(int(input())):
    n=int(input())
    print(euler(n))
    print("Case "+str(i+1)+":"+str((n-euler(n))*2))


'''
'''


ph=[0]*10000000

def phi(n):
    for i in range(1,10000000):
        ph[i]=i 
    
    for i in range(2,n+1):
        if ph[i]==i:
            for j in range(i,n+1,i):
                ph[j]*=(i-1)
                ph[j]//=i
    return ph[n]


for _ in range(int(input())):
    n=int(input())
    phi(n)
    h=0
    for i in range(1,n+1):
        if str(i)==str(ph[i])[::-1]:
            h=i 
    print(h)
        
        
    #print(h)
    '''
'''
    m=0
    x=0
    for i in range(1,n+1):
        if str(i)==str(ph[i])[::-1]:
            if m<=len(str(i)):
                m=len(str(i))
                if x<i:
                    x=i
    print(x)
    #print("--->",ph[291])

    '''

'''
for _ in range(int(input())):
    N=int(input())
    chef=0 
    chefu=0
    for _ in range(N):
        g,a,b=map(int,input().split())
        chef+=((a/(a+b))*g)
        chefu+=((b/(a+b))*g)

    print(float(chefu),float(chef))
'''
'''
def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=[]
    x=0
    m=0
    for i in range(1,n+1):
        if countSetBits(i)==k:
            ans.append(i)
    for v in ans:
        s=0
        for j in range(n):
            s+=(v&a[j])
        if m<s:
            m=s 
            x=v
        elif m==s:
            if x>v:
                x=v 
    print(x)
        

'''



  

'''
for _ in range(int(input())):
    s,n=map(int,input().split())
    coin=0
    if s%2!=0:
        coin+=1
        s-=1 
        r=s%n 
        v=s//n
        coin+=v 
        if r!=0:
            coin+=1 
        print(coin) 
    else:
        r=s%n 
        v=s//n
        coin+=v 
        if r!=0:
            coin+=1
        print(coin)
'''




'''
phi=[0]*10000
def ph(n):

    for i in range(1,n+1):
        phi[i]=i
    
    for i in range(2,n+1):
        if phi[i]==i:
            for j in range(i,n+1,i):
                phi[j]//=j
                phi[j]*=(i-1)

    return phi[n]

def euler(n):
    res=n
    i=2
    while i*i<=n:
        if n%i==0:
            res//=i 
            res*=(i-1)
        
        while n%i==0:
            n//=i 
        i+=1
    
    if n>1:
        res*=(n-1)
        res//=n
    return res 

for _ in range(int(input())):
    n=int(input())
    print(euler(n))
    #print(ph(n))


'''








''''

def gcd(a,b,x,y):
    if b==0:
        x=1 
        y=0
        return a
    
    x1=0
    y1=0

    d=gcd(b,a%b,x1,y1)
    x=y1 
    y=x1-y1*(a//b)

    return d 

def findSolution(a,b,c,x,y):
    g=gcd(a,b,x0,y0)
    print(x,y)
    if c%g!=0:
        return False 
    x*=(c//g)
    y*=(c//g)
    if a<0:x=-x 
    if b<0:y=-y 
    return True 

for i in range(int(input())):
    a,b,c=map(int,input().split())
    x0=0
    y0=0
    if findSolution(a,b,c,x0,y0):
        print("Case "+str(i+1)+": Yes")
    else:
        print("Case "+str(i+1)+": No")


def add(a):
    a+=10
a=0
add(a)
print(a)
'''