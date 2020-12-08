import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')

'''
for _ in range(int(input())):
    s=0
    n,m,k=map(int,input().split())
 
    s=n//k 
    if s>m:
        print(m)
    elif s==m:
        print(m)
    elif s<m:
        m=m-s 
        if m>1:
            if m<=(k-1):
                print(s-1)
            elif m>(k-1):
                i=0
                while m>(k-1):
                    m=m-(k-1)
                    i+=1
                if m>0:
                    i+=1
                print(s-i)
                
        else:
            print(s-m)
'''
for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    ans=0
    k=0
    for i in range(n):
        s=input()
        dp=[0]*m
        c=0
        st=0
        for i in range(m):
            if s[i]=='.':
                if i>0:
                    dp[i]=dp[i-1]+1
                elif i==0:
                    dp[i]=1
        for i in range(m):
            if dp[i]>1:
                c+=1
                if i<m-1:
                    if dp[i+1]<2:
                        if dp[i]%2==0:
                            if (y*dp[i]//2)<(dp[i]*x):
                                ans+=(dp[i]//2*y)
                            else:
                                ans+=(dp[i]*x)
                        elif dp[i]%2!=0:
                            v=dp[i]//2
                            if (y*v+x)<(dp[i]*x):
                                ans+=(v*y+x)
                            else:
                                ans+=(dp[i]*x)   
                if i==m-1:
                    if dp[i]%2==0:
                        if (y*dp[i]//2)<(dp[i]*x):
                            ans+=(dp[i]//2*y)
                        else:
                            ans+=(dp[i]*x)
                    elif dp[i]%2!=0:
                        v=dp[i]//2
                        if (y*v+x)<(dp[i]*x):
                            ans+=(v*y+x)
                        else:
                            ans+=(dp[i]*x)
                        

            else:
                if m==1:
                    if s[i]=='.':
                        st+=1
                else:
                    if i<m-1:
                        if dp[i]==1 and dp[i+1]==0:
                            st+=1
                            
                    if i==(m-1):
                        if dp[i-1]==0 and dp[i]==1:
                            st+=1
        ans+=(st*x)

    print(ans)

                
    