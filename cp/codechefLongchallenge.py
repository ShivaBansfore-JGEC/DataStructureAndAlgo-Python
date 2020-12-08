import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r') 

'''
for _ in range(int(input())):
    n=int(input())
    coin=list(map(int,input().split()))
    no_money=0
    chef_purse=0 
    flag=1
    for i in coin:
        if no_money==0:
            if i==5:
                chef_purse+=i
                no_money=1 
                continue
            else:
                flag=0
                break
        if no_money==1:
            if chef_purse>=(i-5):
                chef_purse-=(i-5)
                chef_purse+=i
            else:
                flag=0
                break 
    if flag==1:
        print("YES")
    else:
        print("NO")
'''
def check(i,ts):
    while ts%2==0:
        if i%2!=0:
            break
        i=i//2
        ts=ts//2
    if ts%2!=0 and i%2==0:
        return True 
    else:
        return False 

for _ in range(int(input())):
    ts=int(input())
    if ts<=2:
        print(0)
    elif ts%2!=0:
        print((ts-1)//2)
    elif ts%2==0:
        t=ts
        c=0
        s=0
        while ts%2==0:
            s+=1
            ts=ts//2
        for i in range(2,ts,4):
            #if check(i,ts):
            v=i//s
            if v%2==0:
                c+=1
        print(c)
