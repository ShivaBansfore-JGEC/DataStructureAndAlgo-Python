import sys
sys.stdout = open('dynamic_programming/output.txt', 'w')
sys.stdin = open('dynamic_programming/input.txt', 'r')
def printdp(dp):
    for i in range(11):
        for j in range(2):
            for k in range(2):
                print(dp[i][j][k],end=" ")
            print()
#printdp()
def f(s,pos=0,tight=1,flag=0):
    if pos==len(s):
        if flag==1:
            return 1
        else:
            return 0
    if dp[pos][tight][flag]!=-1:
        return dp[pos][tight][flag]
    lmt=0
    if tight==1:
        lmt=int(s[pos])+1

    if tight==0:
        lmt=10
    res=0
    for i in range(lmt):
        flg=flag
        if i==3:
            flg=1
        if i == int(s[pos]):
            res+=f(s,pos+1,1,flg)
        else:
            res+=f(s,pos+1,0,flg)

    dp[pos][tight][flag]=res 
    return dp[pos][tight][flag]

for _ in range(int(input())):
    n=int(input())
    dp=[[[-1 for x in range(2)] for y  in range(2)] for z in range(11)]
    print(n-f(str(n)))
    printdp(dp)