g = {
	0: [1,2,3],
	1: [0,2,4],
	2: [0,1,4],
	3: [0,4],
	4: [1,2,3]
}

visited = [0 for i in range(5)]

def dfs(s):
	visited[s]=1
	print(s," --->")
	for i in g[s]:
		if visited[i]==0:
			dfs(i)

print(dfs(0))