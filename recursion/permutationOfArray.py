import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def permutation(arr,start,res):
    if start>=len(arr):
        res.append(arr.copy())
        return 

    for i in range(start,len(arr)):
        swap(arr,start,i)
        permutation(arr,start+1,res) 
        swap(arr,start,i)
        


a=list(map(int,input().split()))
res=[]
permutation(a,0,res)
for x in res:
     print(x)
