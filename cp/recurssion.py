import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')
'''
def path(cr,cc,er,ec):
    if  cr==er and cc==ec:
        return 1 
    if cr>er or cc>ec:
        return 0
    p1= path(cr,cc+1,er,ec)
    p2=path(cr+1,cc,er,ec)
    return p1+p2 

for _ in range(int(input())):
    n,m=map(int,input().split())
    print(path(1,1,n,m))
'''

def s(arr,ci,ans,si):
    if ci>=len(arr):
        print(ans[:si])
        return 
    s(arr,ci+1,ans,si)
    ans[si]=arr[ci]
    s(arr,ci+1,ans,si+1)

    





a=list(map(int,input().split()))
ans=[-1]*len(a)
s(a,0,ans,0)