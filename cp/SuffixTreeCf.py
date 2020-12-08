import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')


def suffixArray(pattern):
    lps=[0]*len(pattern)
    i=1
    j=0
    while i < len(pattern):
        if pattern[i]==pattern[j]:
            lps[i]=j+1
            i+=1
            j+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                lps[i]=j
                i+=1
    return lps

def KMP(text,pattern):
    lps=suffixArray(pattern)
    i=0
    j=0
    while i < len(text):
        if text[i]==pattern[j]:
            i+=1
            j+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
        if j==len(pattern):
            return True
    return False 

def allChar(s,t):
    for i in t:
        if i not in s:
            return False
    return True 

def checkoeder(s,t):
    i=0
    j=0
    while i  < len(s):
        if s[i]==t[j]:
             j+=1
        if j==len(t):
            return True
        i+=1
    return False 


s=input()
t=input()
if checkoeder(s,t) and len(s) > len(t):
    print("automaton")
elif allChar(s,t)==True and len(s)==len(t):
    print("array")
elif allChar(s,t)==True and checkoeder(s,t)==False:
    print("both")
elif allChar(s,t)==False:
    print("need tree")

