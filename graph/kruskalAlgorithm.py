import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')
class edge:
    def __init__(self):
        self.src=None 
        self.dst=None
        self.wt=None 
def sort_wt(obj1):
    return obj1.wt
def findParent(v,parent):
    if parent[v]==v:
        return v 
    return findParent(parent[v],parent)

def kruskal(inputar,n,e):
    #sort the input arr 
    sorted(inputar,key=lambda x: x.wt)
    for i in range(n):
        print(inputar[i].wt,end=" ")
    print()
    mst=[None]*(n-1)

    #parent array
    parent=[0]*n 
    for i in range(n):
        parent[i]=i 
    
    #now adding edges to mst 
    i=0
    count=0
    while count!=n-1:
        currentEdge=inputar[i]

        #check if we can add the current edge in mst or nor 
        sourceParent=findParent(currentEdge.src,parent)
        dstParent=findParent(currentEdge.dst,parent)

        if sourceParent!=dstParent:
            mst[count]=currentEdge
            count+=1
            parent[sourceParent]=dstParent
        i+=1

    for i in range(n-1):
        if mst[i].src<mst[i].dst:
            print(mst[i].src,mst[i].dst,mst[i].wt)
        else:
            print(mst[i].dst,mst[i].src,mst[i].wt)



n,e=map(int,input().split())
inputar=[None]*e
for i in range(e):
    s,d,w=map(int,input().split())
    e=edge()
    e.src=s
    e.dst=d
    e.wt=w
    inputar[i]=e 
kruskal(inputar,n,e)


