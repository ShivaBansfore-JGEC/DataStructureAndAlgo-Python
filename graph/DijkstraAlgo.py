import sys
sys.stdout = open('graph/output.txt', 'w')
sys.stdin = open('graph/input.txt', 'r')
from collections import defaultdict
class test:
    def __init__(self):
        self.cost=0



class Heap:

    def __init__(self):
        self.items=[]
        self.map={}
    
    def getSize(self):
        return len(self.items)
    
    #insert method

    def insert(self,data):
        self.items.append(data)
        self.map[data]=len(self.items)-1
        self.upheapify(len(self.items)-1)
    

    #upheapify 
    
    def upheapify(self,ci):
        pi=int((ci-1)/2)
        #print("hii")
        if self.items[ci].cost<self.items[pi].cost and pi>=0 and ci>=0 and pi<len(self.items) and ci<len(self.items):
            self.swap(ci,pi)
            self.upheapify(pi)


    #down heapify 

    def downheapify(self,pi):
        lci=2*pi+1
        rci=2*pi+2
        mini=pi

        if lci<len(self.items) and self.items[lci].cost<self.items[mini].cost:
            mini=lci 
        if rci<len(self.items) and self.items[rci].cost<self.items[mini].cost:
            mini=rci 

        if mini!=pi:
            self.swap(pi,mini)
            self.downheapify(mini)
    
    def delete(self):
        self.swap(0,(len(self.items)-1))
        rv=self.items[len(self.items)-1]
        self.items.remove(self.items[len(self.items)-1])
        self.downheapify(0)
        return rv

    def updatePriority(self,pair):
        index=self.map[pair]
        self.upheapify(index)


    def swap(self,i,j):
       #print("hell")
        self.items[i],self.items[j]=self.items[j],self.items[i]
    
    def printHeap(self):
        for obj in self.items:
            print(obj.cost,end=" ")

#heap.delete()
#heap.printHeap()


#------------ DIJKSTRA ALGORITHM --------
graph=defaultdict(list)
n=int(input())
wt=list(map(int,input().split()))
i=0
for _ in range(n):
    u,v=map(str,input().split())
    m1={}
    m2={}
    m1[v]=wt[i]
    m2[u]=wt[i]
    graph[u].append(m1)
    graph[v].append(m2)
    i+=1


class disktraPair:
    def __init__(self):
        self.name=""
        self.psf=""
        self.cost=None
print(graph)
def dijkstra(src):
    map={}
    ans={}
    heap=Heap()

    keys=graph.keys()

    for key in keys:
        np=disktraPair()
        np.name=key 
        np.psf=""
        np.cost=float('inf')

        if key==src:
            np.cost=0
            np.psf=src 
        heap.insert(np)
        map[key]=np
    while heap.getSize()>0:
        rp=heap.delete()
        del map[rp.name]
        ans[rp.name]=rp.cost
        nbr=graph[rp.name]
        for key in nbr:
            k=key.keys()
            for ky in k:
                if ky in map:
                    oc=map[ky].cost 
                    nc=rp.cost+key[ky]

                    if nc<oc:
                        gp=map[ky]
                        gp.psf=rp.psf+ky 
                        gp.cost=nc 

                        heap.updatePriority(gp)
                    

    return ans





print(dijkstra("A"))
    

