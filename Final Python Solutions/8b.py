n = 5
graph={
    1:{ 2:10, 5:100},
    2:{ 1:10, 3:50},
    3:{ 2:50, 4:20, 5:10},
    4:{ 3:20, 5:60},
    5:{ 1:100, 3:10, 4:60}
}
dist , path = {}, {}
for i in range(1, n + 1):
	dist[i] = 999
	path[i] = []
src = int(input('Enter source node: '))
log = []
Spt = [src]
dist[src] = 0
path[src] = [src]
for j in graph[src].keys():
	if j not in Spt:
		if dist[j] > dist[src] + graph[src][j]:
			path[j] = path[src] + [j]
		dist[j] = min(dist[j], (dist[src] + graph[src][j]))
print()
while (len(Spt)!=n):
	i = sorted(dist, key=dist.get)[len(Spt)]
	Spt.append(i)
	print('\n', i, dist, Spt)
	for j in graph[i].keys():
		if j not in Spt:
			if dist[j] > dist[i] + graph[i][j]:
				path[j] = path[i] + [j]
			dist[j] = min(dist[j], (dist[i] + graph[i][j]))
	log.append(dist)
print(path)
print('Short path tree is:', Spt)
print('min distances:\n', log[-1])
