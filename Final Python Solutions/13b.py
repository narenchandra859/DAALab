def ginput():
    print("Enter edges with wt, -1 to stop: ")
    while(1):
        x=[int(a) for a in input().split()]
        if x[0]==-1:
            break
        G.append([x[0],x[1],x[2]])

def bellford(n,s):
    d=[999 for x in range(n+1)]
    d[s]=0
    path={}
    path[s]=[s]
    for i in range(n-1):
        for p in G:
            (u,v,w)=p
            if(d[v]>d[u]+w):
                path[v]=path[u]+[v]
            d[v]=min(d[v],d[u]+w)
    print("paths = ",path)
    del(d[0])
    print("distances = ",d)
n=int(input("Enter number of vertices : "))
G=[]
ginput()
s=int(input("Enter starting node : "))
bellford(n,s)