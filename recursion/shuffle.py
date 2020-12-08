import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

li=0
def suffle(arr,si,n,ans):
    global li 
    if si==n:
        return ans

    suffle(arr,si+1,n,ans) 

    if li<si:
        ans.append(arr[si])
        ans.append(arr[(n//2)-li-1])
        li+=1
    return ans
for _ in range(int(input())):
    n=int(input())
    a=[]
    arr=list(map(int,input().split()))
    print(suffle(arr,0,n,a)[::-1])
    li=0

