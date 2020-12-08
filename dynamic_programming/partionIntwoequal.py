import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')

def partion(a,n,sum,dp):
    if sum==0:
        return True 
    if n==0 and sum!=0:
         return False 

    if dp[n]==True:
        return dp[n]
    if a[n]>sum:
        return partion(a,n,sum,dp) 
    
    dp[n]=partion(a,n-1,sum,dp) or partion(a,n-1,sum-a[n],dp)
    return dp[n]



a=list(map(int,input().split()))
sum=0
for i in a:
    sum+=i 
if sum%2!=0:
    print(False)
else:
    dp=[False]*len(a)
    print(partion(a,len(a)-1,sum//2,dp))
    print(dp)