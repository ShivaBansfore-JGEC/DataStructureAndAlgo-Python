import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')
count=0
def coinChange(coins,amount,ans,l):
    if amount==0:
        print(ans)
        return 
    
    for i in range(l,len(coins)):
        if amount>=coins[i]:
            coinChange(coins,amount-coins[i],ans+str(coins[i]),i)

notes=list(map(int,input().split()))
amt=int(input())
coinChange(notes,amt,"",0)
