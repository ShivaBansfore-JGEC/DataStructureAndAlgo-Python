import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

def towerOfHonoi(n,src,dest,helper):
    if n==0:
        return 
    
    towerOfHonoi(n-1,src,helper,dest)
    dest.append(src.pop())
    towerOfHonoi(n-1,helper,dest,src)

n=int(input())
src=[]
dest=[]
helper=[]
for i in range(1,n+1):
    src.append(i)

towerOfHonoi(n,src,dest,helper)
print(dest)