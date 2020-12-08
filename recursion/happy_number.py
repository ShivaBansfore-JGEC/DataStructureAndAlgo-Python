import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

'''

def check(n):
    if n==0:
        return False
    else:
        s=sum(int(i)*int(i) for i in str(n))
        if s==4:
            return False
        
        if s==1:
            return True 
        return check(int(s)) 

def happy(n):
    if check(n):
        return n
    
    return happy(n+1)

for _ in range(int(input())):
    n=int(input())
    print(happy(n+1))
'''
def printPattern(n):
    if n<=0:
        return n
    print(n,end=" ")
    m=printPattern(n-5)
    print(m,end=" ")
    m+=5
    return m
    


for _ in range(int(input())):
    n=int(input())
    printPattern(n)
    print(n)