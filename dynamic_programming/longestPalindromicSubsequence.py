import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')


#TOP DOWN APPROACH

def palindrome(st,i,j,dp):
    if i==j:
        return 1
    if i>j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    c=0
    c1=0
    c2=0
    if st[i]==st[j]:
        c=palindrome(st,i+1,j-1,dp)+2
    elif st[i]!=st[j]:
        c1=palindrome(st,i+1,j,dp)
        c2=palindrome(st,i,j-1,dp)
        return max(c1,c2)
    dp[i][j]=c
    return dp[i][j]

#Bottom up dp

def longestPalindrome(s):
    dp=[]
    for _ in range(10):
        dp.append([0]*10)

    n=len(s)
    #base case

    for i in range(n):
        dp[i][i]=1
    
    for l in range(2,n+1):
        for i in range((n-l)+1):
            j=i+l-1
            if s[i]==s[j]:
                dp[i][j]=dp[i+1][j-1]+2
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j-1])
    print(dp)
    return dp[0][n-1]





s=input()
dp=[]
for _ in range(len(s)+1):
    dp.append([-1]*(len(s)+1))
print(palindrome(s,0,len(s)-1,dp))


for i in range(len(s)+1):
    for j in range(len(s)+1):
        print(dp[i][j],end=" ")  
    print()

print(longestPalindrome(s))
