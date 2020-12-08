import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')


def findUnique(a, n, k): 
    INT_SIZE = 8 * sys.getsizeof(int) 
    count = [0] * INT_SIZE 
    for i in range(INT_SIZE): 
        for j in range(n): 
            if ((a[j] & (1 << i)) != 0): 
                count[i] += 1
    res = 0
    for i in range(INT_SIZE): 
        res += (count[i] % k) * (1 << i) 
    return res 

for _ in range(int(input())):
    n=int(input())
    X=[]
    Y=[]
    for _ in range((4*n)-1):
        x,y=map(int,input().split())
        X.append(x)
        Y.append(y)
    print(findUnique(X,len(X),2),findUnique(Y,len(Y),2))
    
    
