import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

def f(n,s,pos=0,prev=0):
    if n==pos:
        return 1 
    res=0
    for i in range(len(s)):
        if prev==0 or abs(prev-s[i])<=2:
            res+=f(n,s,pos+1,s[i])
    return res 

for _ in range(int(input())):
    m,n=map(int,input().split())
    s=list(map(int,input().split()))
    d=[[-1 for x  in range(12)] for y in range(12)]
    ans=f(n,s)
    print(ans)