import sys
import math

m,n=map(int,input().split())

if m==n:
    print(0)
elif m>n:
    if(m%n==0):
        ls=[]
        ls.append(n)
        res=n
        while(res<m):
            res*=2
            ls.append(res)
        print(len(ls)-1)
    else:
        l1=[]
        l2=[]
        l1.append(1)
        l1.append(m)

        l2.append(1)
        l2.append(n)
        for i in range(2,int(math.sqrt(m))+1):
            if(m%i==0):
                if(i!=m//2):
                    l1.append(i)
                    l1.append(m//i)
                else:
                    l1.append(i)

        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                if(i!=n//i):
                    l2.append(i)
                    l2.append(n//i)
                else:
                    l2.append(i)
        
        l1.sort()
        l1.reverse()
        ans1=[]
        ans1.append(m)
        ans1.append(l1[1])
        for i in range(1,len(l1)-1):
            if l1[i]%l1[i+1]!=0:
                break;
            else:
                ans1.append(l1[i+1])
        if 1 not in ans1:
            ans1.append(1)

        l2.sort()
        l2.reverse()
        ans2=[]
        ans2.append(n)
        ans2.append(l2[1])
        for i in range(1,len(l2)-1):
            if l2[i]%l2[i+1]!=0:
                break;
            else:
                if l2[i+1] not in ans2:
                    ans2.append(l2[i+1])
        if 1 not in ans2:
            ans2.append(1)

        uncommon=0
        common=0
        for a in ans1:
            if a not in ans2:
                uncommon+=1
            else:
                common+=1
        for b in ans2:
            if b not in ans1:
                uncommon+=1
        print(uncommon+common-1)


else:
    if(n%m==0):
        ls=[]
        ls.append(m)
        res=m
        while(res<n):
            res*=2
            ls.append(res)
        print(len(ls)-1)
    else:
        l1=[]
        l2=[]
        l1.append(1)
        l1.append(n)

        l2.append(1)
        l2.append(m)
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                if(i!=n//2):
                    l1.append(i)
                    l1.append(n//i)
                else:
                    l1.append(i)

        for i in range(2,int(math.sqrt(m))+1):
            if(m%i==0):
                if(i!=m//i):
                    l2.append(i)
                    l2.append(m//i)
                else:
                    l2.append(i)

        l1.sort()
        l1.reverse()
        ans1=[]
        ans1.append(n)
        ans1.append(l1[1])
        for i in range(1,len(l1)-1):
            if l1[i]%l1[i+1]!=0:
                break;
            else:
                ans1.append(l1[i+1])

        if 1 not in ans1:
            ans1.append(1)

        l2.sort()
        l2.reverse()
        ans2=[]
        ans2.append(m)
        ans2.append(l2[1])
        for i in range(1,len(l2)-1):
            if l2[i]%l2[i+1]!=0:
                break;
            else:
                ans2.append(l2[i+1])
        
        if 1 not in ans2:
            ans2.append(1)

        uncommon=0
        common=0
        for a in ans1:
            if a not in ans2:
                uncommon+=1
            else:
                common+=1
        for b in ans2:
            if b not in ans1:
                uncommon+=1
        print(uncommon+common-1)