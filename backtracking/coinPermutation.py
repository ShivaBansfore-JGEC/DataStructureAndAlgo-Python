import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')

def coinPermutation(coin,amount,ans):
    if amount==0:
        print(ans)
    
    for i in range(len(coin)):
        if amount>=coin[i]:
            coinPermutation(coin,amount-coin[i],ans+str(coin[i]))

coin=list(map(int,input().split()))
amount=int(input())
coinPermutation(coin,amount,"")