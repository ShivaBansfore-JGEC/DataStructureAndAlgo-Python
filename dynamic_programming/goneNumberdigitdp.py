import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

primes=[2,5,7,11,13,17,19,23,29,31,41,43,47,53,59,61,67,69,71,73,79,83,89]
def check(sum):
    if sum in primes:
        return True 
    else:
        return False 
def g(s,pos,tight,sum):
    if pos==len(s):
        if check(sum):
            return 1
        else:
            return 0
    
    lmt=0
    if tight==1:
        lmt=int(s[pos])+1
    if tight==0:
        lmt=10

    res=0
    for i in range(lmt):
        if i==int(s[pos]):
            res+=g(s,pos+1,1,sum+i)
        else:
            res+=g(s,pos+1,0,sum+i)
    return res

for _ in range(int(input())):
    dp=[[[-1 for x in range(2)] for y in range(80)] for z in range(10)]
    l,r=map(int,input().split())
    l=l-1
    a=str(l)
    b=str(r)

    ans1=g(b,0,1,0)
    ans2=g(a,0,1,0)
    print(ans1,ans2)
    print(ans1-ans2)