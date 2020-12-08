import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')

def queenPermatation(box,qpsf,tq,ans):
    if qpsf==tq:
        print(ans)
        return 
    for i in range(len(box)):
        if box[i]==False:
            box[i]=True
        queenPermatation(box,qpsf+1,tq,ans+"q"+str(qpsf)+"b"+str(i)+" ")
        box[i]=False
n=int(input())
q=int(input())
box=[False]*n 

queenPermatation(box,0,q,"")

