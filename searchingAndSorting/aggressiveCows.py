import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

def possible(stall,c,d):
    cow=1;pos=stall[0]
    for i in range(1,len(stall)):
        if stall[i]-pos>=d:
            pos=stall[i]
            cow+=1
            if cow==c:
                return True 
    return False




def binarySearch(stall,cow):
    final_ans=-1
    l=0
    r=max(stall)-1

    while l<=r:
        mid=l+((r-l)//2) 
        if possible(stall,cow,mid):
            #move right 
            final_ans=mid 
            l=mid+1 
        else:
            r=mid-1 
    return final_ans


for _ in range(int(input())):
    n,c=map(int,input().split())
    stall_pos=[]
    for _ in range(n):
        stall_pos.append(int(input()))
    stall_pos.sort()
    print(binarySearch(stall_pos,c))