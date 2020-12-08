import sys
import math
sys.stdout = open('Strings/output.txt', 'w')
sys.stdin = open('Strings/input.txt', 'r')
p=31
m=1000000009
def has_function(s,n):
    has_val=0
    p_pow=1
    for i in range(n):
        has_val=(has_val+(ord(s[i])-ord('a')+1)*p_pow)%m 
        p_pow=(p*p_pow)%m 

    return has_val 


def recalculateHash(txt,oldHash,oldIndex,newIndex,patLen):
    newHash=oldHash-(ord(txt[oldIndex])-ord('a')+1)
    newHash//=p 
    newHash+=((ord(txt[newIndex])-ord('a')+1)*pow(p,patLen-1))
    return newHash 

def check(s,t,s1,e1 ,s2,e2):
    if e1-s1!=e2-s2:
        return False 

    while s1<=e1 and s2<=e2:
        if s[s1]!=t[s2]:
            return False 
        s1+=1
        s2+=1
    return True 

def main():
    s=input()
    pat=input()
    n=len(pat)
    patHash=has_function(pat,n)
    strHash=has_function(s,n)
    for i in range(len(s)-len(pat)):
        if patHash==strHash and check(s,pat,i,i+(n-1) ,0,n-1):
            print("the match found at",i)
        else:
            strHash=recalculateHash(s,strHash,i,i+n,n)
            
main()
