import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')

def isSafe(mat,visited,x,y):
    return not(mat[x][y]==0 or visited[x][y])

def isValid(x,y):
    return M>x>=0 and N>y>=0

def longestpath(mat,visited,cr,cc,er,ec,mxds,ds):
    if mat[cr][cc]==0:
        return 0

    if cr==er and cc==ec:
        return max(mxds,ds)

    visited[cr][cc]=1

    # go to bottom 
    if isValid(cr+1,cc) and isSafe(mat,visited,cr+1,cc):
        mxds=longestpath(mat,visited,cr+1,cc,er,ec,mxds,ds+1)

    # go to right 
    if isValid(cr,cc+1) and isSafe(mat,visited,cr,cc+1):
        mxds=longestpath(mat,visited,cr,cc+1,er,ec,mxds,ds+1)
 
    # go to top  
    if isValid(cr-1,cc) and isSafe(mat,visited,cr-1,cc):
        mxds=longestpath(mat,visited,cr-1,cc,er,ec,mxds,ds+1)

 
    #go to left
    if isValid(cr,cc-1) and isSafe(mat,visited,cr,cc-1):
        mxds=longestpath(mat,visited,cr,cc-1,er,ec,mxds,ds+1)
 
    visited[cr][cc]=0

    return mxds
            

N=M=10 
visited=[[0 for x in range(N)] for y in range(N)]

mat = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]
print(longestpath(mat,visited,0,0,5,7,0,0))