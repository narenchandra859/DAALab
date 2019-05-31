def graph_input():
    print("Enter edges with weight(X,Y,W)[-1 to stop]: ")
    while(1):
        e=[int(x) for x in input().split()]
        if e[0]==-1:
            break
        if e[0] in graph.keys():
            graph[e[0]].append(e[1])
        else:
            graph[e[0]] = [e[1]]
        if e[1] in graph.keys():
            graph[e[1]].append(e[0])
        else:
            graph[e[1]] = [e[0]]
        weight[e[0],e[1]] = weight[e[1],e[0]] = e[2]
def min_edge(vt,ut):
    global cost
    min_wt = 999
    min_edge = []
    for i in vt:
        for j in graph[i]:
            if j in ut and weight[i,j]<min_wt:
                min_edge = [i,j]
                min_wt = weight[i,j]
    cost=cost+min_wt
    return min_edge
def prim():
    mst = []
    vt = [sorted(graph.keys())[0]]               #INITIALLY set of visited vertices = 1st vertex
    ut = [x for x in graph.keys() if x not in vt] #Set of unvisited vertices
    for i in range(0,len(graph.keys())-1):       #iterate till number of edges = |V| - 1
        edge = min_edge(vt,ut)
        vt.append(edge[1])          #add v to set set of visited vertices
        ut.remove(edge[1])          #remove v from set of unvisited vertices
        mst.append(edge)            #add edge to mst
    return mst
cost=0
(graph,weight) = ({},{})
graph_input()
print(graph,weight)
mst = prim()
print(mst)
print("Minimum cost = ",cost)