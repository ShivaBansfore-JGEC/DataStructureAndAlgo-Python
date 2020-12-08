import sys
sys.stdout = open('backtracking/output.txt', 'w')
sys.stdin = open('backtracking/input.txt', 'r')

def queencombination(box,qpsf,tq,ans,lastBoxUsed):
    if qpsf==tq:
        print(ans)
        return 
    for i in range(lastBoxUsed+1,len(box)):
        if box[i]==False:
            box[i]=True
        queencombination(box,qpsf+1,tq,ans+"q"+str(qpsf)+"b"+str(i)+" ",i)
        box[i]=False 
n=int(input())
q=int(input())
box=[False]*n 
queencombination(box,0,q,"",-1)


