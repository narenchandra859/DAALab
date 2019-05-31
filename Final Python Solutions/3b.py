import time as t
import random as r
def InsSort(l):
	for i in range(1,len(l)):
		p = i
		while l[p]<l[p-1] and p>0:
			l[p],l[p-1]=l[p-1],l[p]
			p = p - 1
	return(l)
x = [r.randint(0,1000) for y in range(50)]
print(x)
s = t.time()
x = InsSort(x)
print(x)
print("Time taken = ",t.time()-s)