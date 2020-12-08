import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')


def p(grid,n,m):
    print()
    for i in range(n):
        for j in range(m):
            print(grid[i][j],end=" ")
        print()

def ratInMaze(grid,maze,cr,cc,er,ec):
    if cr==er and cc==ec:
        maze[cr][cc]=1
        for i in range(er+1):
            for j in range(cc+1):
                print(maze[i][j],end=" ")
            print()
        return True

    if cr>er or cc>ec:
        return False 

    if grid[cr][cc]=='X':
        return False 

    maze[cr][cc]=1
    right_succes=ratInMaze(grid,maze,cr,cc+1,er,ec)
    if right_succes:
        return True
    
    down_success=ratInMaze(grid,maze,cr+1,cc,er,ec)
    if down_success:
        return True
    
    #Backtrack 
    maze[cr][cc]=0
    return False








maze=[
    ['O','X','O','O'],
    ['O','O','O','X'],
    ['O','O','X','O'],
    ['X','O','O','O'],
    ['X','X','O','O']
]
n,m=map(int,input().split())
sol=[]
for i in range(n):
    sol.append([0]*m)
print(ratInMaze(maze,sol,0,0,n-1,m-1))

