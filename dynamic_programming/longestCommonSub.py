import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')


#TOP DOWN SOLUTION
def longestCommonSub(s,o,i,j,dp):
    if s[i]=='0' or o[j]=='0':
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i]==o[j]:
        dp[i][j]=1+longestCommonSub(s,o,i+1,j+1,dp)
        return dp[i][j]
    else:
        dp[i][j]=max(longestCommonSub(s,o,i+1,j,dp),longestCommonSub(s,o,i,j+1,dp))
        return dp[i][j]

#BOTTOM UP SOLUTION

def LongestCommonsubBU(s,o,r,c):
    dp=[[0 for i in range(c)] for j in range(r)]

    for i in range(r):
        for j in range(c):
            if s[i]==s[j]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    for i in range(r):
        for j in range(c):
            print(dp[i][j],end=" ")
        print()
    return dp[r-1][c-1]



s=input()
o=input()
dp=[[-1 for i in range(len(o))] for j in range(len(s))]
#print(longestCommonSub(s,o,0,0,dp))

print(dp)
print(LongestCommonsubBU(o,s,len(o),len(s)))