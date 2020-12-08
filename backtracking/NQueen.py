import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')

def isSafe(board,r,c):

    #checking row of board 
    i=r 
    while i>=0:
        if board[i][c]:
            return False 
        i-=1

    
    #checkinf upper left triange 
    i=r 
    j=c
    while i>=0 and j>=0:
        if board[i][j]:
            return False 
        i-=1
        j-=1
    
    #checking upper right triangle 

    i=r 
    j=c
    
    while i>=0 and j<len(board):
        if board[i][j]:
            return False
        i-=1
        j+=1 


    return True

def Nqueen(box,r):
    if r==len(box):
        return 1
    count=0

    for c in range(len(box[r])):
        if isSafe(box,r,c):
            box[r][c]=True
            count=count+Nqueen(box,r+1)
            box[r][c]=False
    return count 

n=int(input())
board=[]
for _ in range(n):
    board.append([False]*n)

print(Nqueen(board,0))