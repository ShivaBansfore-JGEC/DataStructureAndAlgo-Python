import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')
print("hello")



'''
s=0
pos=0
n=int(input())
for i in range(n):
    h=int(input())
    if i<n-1:
        if pos==0:
            s+=(h)+2
            pos=h 
        else:
            if pos>h:
                s+=(pos-h)+2 
                pos=h
            elif pos<h:
                s+=(h-pos)+2 
                pos=h
            else:
                s+=2 
                pos=h 
    else:
        if pos>h:
            s+=(pos-h)+1 
            pos=h
        elif pos<h:
            s+=(h-pos)+1 
            pos=h
        else:
            s+=1
            pos=h 

    
print(s)
'''