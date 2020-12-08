import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')

# Below lists details all 8 possible movements for a knight.
# Don't change the sequence of below lists
row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]

def isValid(x,y):
    if (x>=0 and x<N) and (y>=0 and y < N):
        return True 
    else:
        return False

def knightTour(chess,x,y,pos):
    chess[x][y]=pos

    if pos>=N*N:
        print()
        for i in range(N):
            for j in range(N):
                print(chess[i][j],end=" ")
            print()

        
        chess[x][y]=0
        return 
    
    for j in range(8):
        xx=x+row[j]
        yy=y+col[j]

        if isValid(xx,yy) and chess[xx][yy]==0:
            knightTour(chess,xx,yy,pos+1)
    
    chess[x][y]=0







N=int(input())
chess=[[0 for x in range(N)] for y in range(N)]
pos=1
knightTour(chess,0,0,pos)