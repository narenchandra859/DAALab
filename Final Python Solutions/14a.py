import time as t
import random as r
def selsort(A):
	for i in range(0,len(A)-1):
		min = i
		for j in range(i,len(A)-1):
			if A[j] < A[min]:
				min = j
		A[min],A[i] = A[i],A[min]
	return A
x = [r.randint(0,1000) for y in range(0,500)]
s = t.time()
print(x[:25])
print("Sorting..")
x = selsort(x)
print(x[:25])
print("Time taken = ",t.time()-s)