import sys
sys.stdout = open('cp/output.txt', 'w')
sys.stdin = open('cp/input.txt', 'r')

n,w,d=map(int,input().split())
a=list(map(int,input().split()))

A_move=(n-n//w)//w
B_move=(n-n//(w+d))//w+d
print(B_move)
