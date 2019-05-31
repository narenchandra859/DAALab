g = {
	1: [2,3,4],
	2: [3,5],
	3: [4,5],
	4: [3,5],
	5: []
}
visited = [0 for i in range(6)]
def BFS(s):
	level = [[s]]
	visited[s]=1
	print(" --->",s)
	i = 0
	while(level[i]):
		level.append([])
		for node in level[i]:
			for nodes in g[node]:
				if visited[nodes]==0:
					print("--->",nodes)
					visited[nodes]=1
					level[i+1].append(nodes)
		i = i + 1

BFS(1)
