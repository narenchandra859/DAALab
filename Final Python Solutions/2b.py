import time as t
def menEngaged():
	for v in man.values():
		if v[1]==0:
			return 1
	return 0

def propose():
	for x, y in man.items():
		if y[1]==0:
			m = x
			break
	prefList = man[m][0]
	for i in prefList:
		if women[i][1] == 0:
			pairs.append((m,i))
			women[i][1] = m
			man[m][1] = i
			break
		else:
			m1 = women[i][1]
			i1 = women[i][0].index(m1)
			i2 = women[i][0].index(m)
			if i2<i1:
				pairs.remove((m1,i))
				pairs.append((m,i))
				man[m1][1]=0
				women[i][1] = m
				man[m][1] = i
				break
			else:
				continue


def galeShapely():
	while(menEngaged()):
		propose()
	print("Final pairs = ",pairs)

man = {
	#1 : [[1,2,3],0],					# small example
	#2 : [[2,1,3],0],
	#3 : [[1,2,3],0]
	1: 	[[2,1,4,5,3],0],     # big example
	2:	[[4,2,1,3,5],0],
	3:	[[2,5,3,4,1],0],
	4:	[[1,4,3,2,5],0],
	5:	[[2,4,1,5,3],0]
}
women = {
	#1 : [[1,2,3],0],					# small example
	#2 : [[2,3,1],0],
	#3	: [[3,1,2],0]
	1: [[5,1,2,4,3], 0],			# big example
	2: [[3,2,4,1,5], 0],
	3: [[2,3,4,5,1], 0],
	4: [[1,5,4,3,2], 0],
	5: [[4,2,5,3,1], 0]
}
pairs = []
galeShapely()