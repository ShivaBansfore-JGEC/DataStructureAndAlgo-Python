import sys
sys.stdout = open('recursion/output.txt', 'w')
sys.stdin = open('recursion/input.txt', 'r')

def permutation(str,ans):
    if len(str)==0:
        print(ans,end=" ")
        return 
    for i in range(len(str)):
        ch=str[i]
        ros=str[0:i]+str[i+1:]
        permutation(ros,ans+ch)


for _ in range(int(input())):
    st=input()
    permutation(st,"")
    print()