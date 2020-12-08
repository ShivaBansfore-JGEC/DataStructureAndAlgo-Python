import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')

import math
for _ in range(int(input())):
    # ashish turn
    f=0
    n=int(input())
    c=0
    if n>2 and n%2!=0:
        c+=1
    else:
        while n>1:
            # check both option
            if n%2!=0:
                c+=1
                break 
            else:
                i=3
                best=1
                while i <=(int(math.sqrt(n))):
                    if n%i==0:
                        res=n//i 
                        if res-1>2 and res%2==0:
                            n=n//i
                            f=1
                            c+=1
                            break 
                    i+=2

                if f!=1:
                    n=n-1
                    f=0
                    c+=1
                else:
                    break 
    if c%2==0:
        print("FastestFinger")
    else:
        print("Ashishgup")

        

        



'''
def gcd(a,b): 
    if (b == 0): 
         return a 
    return gcd(b, a%b)

for _ in range(int(input())):
    n=int(input())
    i=1
    m=1
    while i<=n//2:
        if i*2 <=n:
            a=i
            b=i*2 
            #g=gcd(a,b)
            if m<a:
                m=a 
        i+=1

    print(m)
'''
        


