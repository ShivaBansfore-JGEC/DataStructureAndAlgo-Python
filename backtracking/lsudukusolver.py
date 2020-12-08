
import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')
import math 
def isSafe(box,i,j,k,n):
    #checking coloumn 
    for r in range(n):
        if box[r][j]==k:
            return False 
        if box[i][r]==k:
            return False 

    #checking inner box
    rootn=int(math.sqrt(n))

    boxRow=i//rootn
    boxCol=j//rootn

    b1=boxRow*rootn 
    b2=boxCol*rootn 

    for m in range(b1,b1+rootn):
        for l in range(b2,b2+rootn):
            if box[m][l]==k:
                return False


    return True 


def sudukuSolve(box,i,j,n):

    if i==n:
        return True 
    if j==n:
        return sudukuSolve(box,i+1,0,n)

    for m in range(1,10):
        if box[i][j]==0 and isSafe(box,i,j,m,n):
            box[i][j]=m
            lc=sudukuSolve(box,i,j+1,n)
            if lc:
                return True
            box[i][j]=0

    return False





suduku=[
[ 3, 1, 6, 5, 7, 8, 4, 9, 2 ], 
[ 5, 2, 9, 1, 3, 4, 7, 6, 8 ], 
[ 4, 8, 7, 6, 2, 9, 5, 3, 1 ], 
[ 2, 6, 3, 0, 1, 5, 9, 8, 7 ], 
[ 9, 7, 4, 8, 6, 0, 1, 2, 5 ], 
[ 8, 5, 1, 7, 9, 2, 6, 4, 3 ], 
[ 1, 3, 8, 0, 4, 7, 2, 0, 6 ], 
[ 6, 9, 2, 3, 5, 1, 8, 7, 4 ], 
[ 7, 4, 5, 0, 8, 6, 3, 1, 0 ]

]
s=sudukuSolve(suduku,0,0,9)
print(s)