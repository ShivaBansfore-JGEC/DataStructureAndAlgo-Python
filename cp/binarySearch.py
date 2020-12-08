import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')




def binarySearch(arr,n,k):
    l=0
    h=n-1
    while l<=h:
        mid=(l+h)//2

        if k==arr[mid]:
            return mid 
        elif k<arr[mid]:
            h=mid-1
        else:
            l=mid+1
    return -1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(binarySearch(a,n,k))

