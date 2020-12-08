import sys
import math
sys.stdout = open('Strings/output.txt', 'w')
sys.stdin = open('Strings/input.txt', 'r')

def string_hash(s):
    p=31
    has_value=0
    m=1000000009
    p_pow=1
    for c in s:
        has_value=(has_value+(ord(c)*p_pow))%m 
        p_pow=(p_pow*p)%m
    return has_value 

def store(s):
    n=len(s)
    hash_table=[0]*(n)
    for i in range(n):
        hash_table[i]=string_hash(s[i])
    print(hash_table)




s=input()
print(string_hash(s))
store(s)