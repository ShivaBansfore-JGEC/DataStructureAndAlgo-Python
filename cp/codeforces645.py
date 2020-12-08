import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r') 



# PROBLEM A 

'''
for _ in range(int(input())):
    n,m=map(int,input().split())

    if (n*m)%2==0:
        print((n*m)//2)
    else:
        print((n*m)//2+1)

# PROBLEM B 


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    dp=[0]*n 
    s=1
    for i in range(n):
        if (s+(i))>=a[i]:
            dp[i]=(s+i+1)
    if max(dp)==0:
        print(1)
    else:
        print(max(dp))
# PROBLEM C
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    m1=abs(c-a)
    m2=abs(d-b)
    print(m1*m2+1)
'''
n,x=map(int,input().split())
a=list(map(int,input().split()))
a=a+a 
prefixSum=[0]*len(a)
prefixSum[0]=int(a[0]/2*(2+(a[0]-1)*1))
for i in range(1,len(a)):
    prefixSum[i]=int(prefixSum[i-1]+(a[i]/2*(2+(a[i]-1)*1)))
psum=[0]*len(a)
psum[0]=a[0]
for j in range(1,len(a)):
    psum[j]=psum[j-1]+a[j]
print(prefixSum)
print(psum)




