def G_input(G):
    print("Enter the edges. -1 to stop")
    while(1):
        x=[int(a) for a in input().split()]
        if x[0]==-1:
            break
        if x[0] in G.keys():
            G[x[0]].append(x[1])
        else:
            G[x[0]]=[x[1]]
        if x[1] in G.keys():
            G[x[1]].append(x[0])
        else:
            G[x[1]]=[x[0]]
    print("Adjacency list -> ",G)
def DFS(G,s):
    global visited
    visited[s]=True
    print("->",s,end="")
    for x in G[s]:
        if not visited[x]:
            DFS(G,x)
def BFS(G,s):
    v={}
    for i in G.keys():
        v[i]=False
    v[s]=True
    print("->",s)
    level=0
    l=[[s]]
    while(l[level]):
        l.append([])
        for x in l[level]:
            for n in G[x]:
                if not v[n]:
                    v[n]=True
                    print("->",n)
                    l[level+1].append(n)
        level=level+1
G={}
visited={}
n=int(input("Enter number of nodes : "))
G_input(G)
for i in G.keys():
    visited[i]=False
d=int(input("Enter start node for DFS : "))
DFS(G,d)
print()
d=int(input("Enter start node for BFS : "))
BFS(G,d)
print()


