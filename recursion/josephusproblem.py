import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

def josephusProblem(n,k):
    if n==1:
        return 1
    
    else:
        return (josephusProblem(n-1,k)+k-1)%n+1



n,k=map(int,input().split())
print(josephusProblem(n,k))
