import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')
num=[]
def sumOfArray(arr,si,li,ans):
    if si>li:
        num.append(ans)
        return
    sumOfArray(arr,si+1,li,ans+arr[si])
    sumOfArray(arr,si+1,li,ans)

for _ in range(int(input())):
    n=int(input())  
    a=list(map(int,input().split()))
    sumOfArray(a,0,n-1,0)
    num.sort()
    print(*num)
    num=[]

