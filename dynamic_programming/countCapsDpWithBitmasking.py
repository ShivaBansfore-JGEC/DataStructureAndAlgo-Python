import sys
sys.setrecursionlimit(10**9)
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')
from collections import defaultdict

caps=defaultdict(list)
allmask=0
total_caps=100

n=int(input())
for ppl in range(n):
    c=list(map(int,input().split()))
    for i in c:
        caps[i].append(ppl)
allmask=(1<<n)-1

dp=[[-1 for i in range(caps+1)] for j in range(2**n)]


print(allmask)
print(caps)
