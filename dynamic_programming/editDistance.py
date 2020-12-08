import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

#top down 
def editdistance(s1,s2,m,n,dp):
    if m==0:
        return n
    if n==0:
        return m 

    if dp[n-1][m-1]!=-1:
        return dp[n-1][m-1]
    
    
    if s1[m-1]==s2[n-1]:
        dp[n-1][m-1]=editdistance(s1,s2,m-1,n-1,dp) 
        return dp[n-1][m-1]
    dp[n][m]=1+min(editdistance(s1,s2,m,n-1,dp),
                    editdistance(s1,s2,m-1,n,dp),
                    editdistance(s1,s2,m-1,n-1,dp))
    return dp[n-1][m-1]


def bottonUpEdit(s1,s2,m,n):
    dp=[[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    print(dp)
    return dp[m][n]


str1=input()
str2=input()
m=len(str1)
n=len(str2)
dp=[[-1 for i in range(len(str1))] for j in range(len(str2))]
print(editdistance(str1,str2,len(str1),len(str2),dp))
print(dp)
print(bottonUpEdit(str1,str2,m,n))
