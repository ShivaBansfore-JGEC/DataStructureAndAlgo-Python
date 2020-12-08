import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

def toString(b):
    s=""
    for x in b:
        if x=='/0':
            break
        s+=x
    return s

def printString(s,n,i,j,buff):
    #base case
    if i==n:
        buff[j]='/0'
        print(toString(buff))
        return
    #including onlu character 
    buff[j]=s[i]
    printString(s,n,i+1,j+1,buff)

    buff[j]='$'
    buff[j+1]=s[i]
    printString(s,n,i+1,j+2,buff)

for _ in range(int(input())):
    s=input()
    n=len(s)
    buff=[0]*2*n
    buff[0]=s[0]
    printString(s,n,1,1,buff)

