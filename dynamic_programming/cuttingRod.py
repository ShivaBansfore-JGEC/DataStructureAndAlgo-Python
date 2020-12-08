import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')


def cuttingRod(p,n):
    if n<=0:
        return 0 
    max_val=-sys.maxsize-1
    for i in range(n):
        max_val=max(max_val, price[i]+cuttingRod(p,n-i-1))
    return max_val



price=list(map(int,input().split()))
n=len(price)
print(cuttingRod(price,n))