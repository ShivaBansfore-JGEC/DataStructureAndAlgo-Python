import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')

def g(a,b,dp):
    if a<=0 or b<=0:
        return 0
    if dp[a][b]!=-1:
        return dp[a][b]
    ans=0
    ans1=0
    ans1=g(a-1,b-2,dp)+1
    ans=g(a-2,b-1,dp)+1
    dp[a][b]=max(ans,ans1)
    return max(ans,ans1)

for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==0 or b==0:
        print(0)
    elif a==b:
        print(a//2)
    else:
        if a<b:
            a=a//2
            if b>1:
                print(a+1)
            else:
                print(a)
        elif a>b:
            a=a-(b//2)
            b=b-(b//2)

            if a<b:
                a=a//2
                if b>1:
                    print(a+1)
                else:
                    print(a)
            elif a==b:
                print(a+(a//2))
            elif a>b:
                print(a+(a//2))


            
