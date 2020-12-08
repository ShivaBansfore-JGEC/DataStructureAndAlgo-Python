import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

def kPartition(a,si,target,sum,k,used):
    if k==1:
        return True 
    
    if sum>target:
        return False 

    if sum==target:
        return kPartition(a,si,target,sum,k-1,used)
    
    for i in range(si,len(a)):
        if a[i]==True and sum+a[i]<=target:
            used[i]=True 
            sum+=a[i]
            if kPartition(a,si,target,sum,k,used):
                return True 
            used[i]=False 





a=list(map(int,input().split()))
k=int(input())
if sum(a)%k!=0 or k>len(a) or k<=0:
    print(False)
else:
    m=sum(a)//k
    box=[False]*len(a)
    print(kPartition(a,0,m,0,k,box))



