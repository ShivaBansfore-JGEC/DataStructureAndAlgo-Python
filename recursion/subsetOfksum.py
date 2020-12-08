import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

def sumOfsubsetK(a,si,summ,box,total):    
    if summ == m:
        print(summ)
        return 

    if summ>m and total>(m-summ):
        return 
    
    for i in range(si,len(a)):
        if box[i]==0:
            box[i]=1 
            
        summ+=a[i]
        total-=a[i]
        sumOfsubsetK(a,i+1,summ,box,total)
        summ-=a[i]
        total+=a[i]
        box[i]=0

a=list(map(int,input().split()))
m=int(input())
box=[0]*len(a)

sumOfsubsetK(a,0,0,box,sum(a))
