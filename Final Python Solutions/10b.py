def graph_input():
    print("Enter edges with weight(X,Y,W)[-1 to stop]: ")
    while(1):
        e=[int(x) for x in input().split()]
        if e[0]==-1:
            break
        if e[0] not in vertices:
            vertices.append(e[0])
        if e[1] not in vertices:
            vertices.append(e[1])
        graph.append(e)

def kruskal():
    global wt
    mst = []
    for i in vertices:
        parent[i]=0
    (n_edges, i) = (0, 0)                       # n_edges number of edges in mst, i to iterate through edges in graph
    while n_edges < len(vertices) - 1:          # number of edges in mst = |v|-1
        (u, v, w) = graph[i]                    # This is the smallest edge weight
        i += 1
        (a,b,c)=(u,v,w)
        while(parent[u]!=0):
            u=parent[u]
        while(parent[v]!=0):
            v=parent[v]
        if u!=v:                    # if they dont belong to same set (no cycle)
            n_edges += 1
            parent[v]=u
            mst.append([a, b, c])
            wt=wt+w
    return mst
wt=0
(graph, parent, vertices) = ([], {}, [])
graph_input()
print(graph,vertices)
graph.sort(key = lambda x:x[2])                       #Sort the graph based on Edge Weight
mst = kruskal()
print("MST = ",mst)
print("Weight of MST:", wt)