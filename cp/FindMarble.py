import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r') 

n,s,t=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    if s==t:
        print(i)
        break 
    s=a[s-1]
else:
    print(-1)