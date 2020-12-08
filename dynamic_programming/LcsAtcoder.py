import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

def printD(dp,n,m):
    for i in range(m+1):
        for j in range(n+1):
            print(dp[i][j],end=" ")
        print()

def lcs(s,t,i,j,res,dp):
    
    #base case
    if i==len(s) or j==len(t):
        return res 

    if dp[i][j]!="":
        return dp[i][j]

    if s[i]==t[j]:
        return lcs(s,t,i+1,j+1,res+s[i],dp)
    else:
        a=""
        b=""
        
        a=lcs(s,t,i+1,j,res,dp)
        #dp[i][j]=a
        b=lcs(s,t,i,j+1,res,dp)
        #dp[i][j]=b
        if len(a)>=len(b):
            return a 
        else:
            return b 
        


s=input()
t=input()
dp=[[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
#print(lcs(s,t,0,0," ",dp))

for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1]==t[j-1]:
            dp[i][j]=1+(dp[i-1][j-1])
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

x=len(s)
y=len(t)
ans=""
while x!=0 and y!=0:
    if dp[x-1][y]==dp[x][y]:
        x-=1
    elif dp[x][y-1]==dp[x][y]:
        y-=1
    else:
        ans=t[y-1]+ans
        x-=1
        y-=1
print(ans)