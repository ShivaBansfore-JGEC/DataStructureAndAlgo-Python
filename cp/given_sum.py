import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')

def func(pos,arr,summ,n,lis,my_ans,visited):
    if summ==0:
        l1=[]
        if lis:
            for i in lis:
                l1.append(i)
        my_ans.append(l1)
        return my_ans

    for i in range(pos+1,n):
        if(arr[i]<=summ and arr[i] not in visited):
            lis.append(arr[i])
            summ-=arr[i]
            visited.append(arr[i])
            func(i,arr,summ,n,lis,my_ans,visited)
            summ+=arr[i]
            lis.remove(arr[i])
            visited.remove(arr[i])
    return my_ans

def main():
    my_list=[]
    n=int(input())
    for _ in range(n):
        g=int(input())
        wts=list(map(int,input().split()))
        for v in wts:
            my_list.append(v)
    ksum=sum(my_list)//n
    ln=len(my_list)
    ans=[]
    my_ans=[]
    visited=[]
    l=func(-1,my_list,ksum,ln,ans,my_ans,visited)
    final_ans=[]
    for a in l:
        for b in l:
            flag=0
            if(a!=b):
                for i in a:
                    if i in b:
                        flag=1
                        break
        if flag==0:
            final_ans.append(a)
            flag=0
    for ans in final_ans:
        ans.sort()
    final_ans.sort()
    for val in final_ans:
        print(*val)

main()
