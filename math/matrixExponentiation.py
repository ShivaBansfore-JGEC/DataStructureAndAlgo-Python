import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

'''
input:
1
3 3
1 0 4     
1 2 2
0 4 4

'''
def mul(A,B,dim):
    res=[[0 for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                res[i][j]+=A[i][k]*B[k][j]
    
    for i in range(dim):
        for j in range(dim):
            A[i][j]=res[i][j]


def power(arr,dim,n):
    I=[[0 for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if i==j:
                I[i][j]=1 
    


    #NAIVE APPROACH 
    '''
    for _ in range(n):
        mul(I,arr,dim)
    '''

    while n:
        if n%2!=0: 
            mul(I,arr,dim)
            n-=1
        else:
            mul(arr,arr,dim)
            n//=2

    for i in range(dim):
        for j in range(dim):
            arr[i][j]=I[i][j]




def printMat(ar,dim):
    for i in range(dim):
        for j in range(dim):
            print(ar[i][j],end=" ")
        print()

for _ in range(int(input())):
    dim,n=map(int,input().split())
    ar=[]
    for _ in range(dim):
        a=list(map(int,input().split()))
        ar.append(a)
    
    power(ar,dim,n)
    print()
    printMat(ar,dim)