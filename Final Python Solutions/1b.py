def InsSort(l):
	for i in range(1, len(l)):
		p = i
		while l[p] < l[p - 1] and p > 0:
			l[p], l[p - 1] = l[p - 1], l[p]
			p = p - 1
	return(l)

def bucket(l):
	buck = []
	sortL = []
	for i in range(10):
		buck.append([])
	for x in l:
		m = int(x*10)
		buck[m].append(x)
	for b in buck:
		b = InsSort(b)
		sortL.extend(b)
	return(sortL)

print(bucket([0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]))