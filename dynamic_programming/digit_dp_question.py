import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

def f(s,d,k,pos=0,t=1,cnt=0):
    if cnt>k:
        return 0
    if len(s)==pos:
        if cnt==k:
            return 1
        else:
            return 0
    lmt=0

    if t==1:
        lmt=int(s[pos])+1
    if t==0:
        lmt=10
    
    res=0
    for i in range(lmt):
        nf=t
        if i==int(s[pos]):
            nf=1
        else:
            nf=0
        cn=cnt
        if i==d:
            cn+=1
        if cnt<=k:
            res+=f(s,d,pos+1,nf,cn,k)
        return res


for _ in range(int(input())):
    a,b,d,k=map(int,input().split())
    print(f(str(b),d,k)-f(str(a-1),d,k))
