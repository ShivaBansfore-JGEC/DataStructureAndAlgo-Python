


def gcd(a,b,x,y):
    if b==0:
        x=1 
        y=0
        return a
    
    x1=0
    y1=0

    d=gcd(b,a%b,x1,y1)
    x=y1 
    y=x1-y1*(a//b)

    return d 

def findSolution(a,b,c,x,y):
    g=gcd(a,b,x0,y0)
    print(x,y)
    if c%g!=0:
        return False 
    x*=(c//g)
    y*=(c//g)
    if a<0:x=-x 
    if b<0:y=-y 
    return True 

for i in range(int(input())):
    a,b,c=map(int,input().split())
    x0=0
    y0=0
    if findSolution(a,b,c,x0,y0):
        print("Case "+str(i+1)+": Yes")
    else:
        print("Case "+str(i+1)+": No")