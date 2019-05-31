import time as t
import random as r
def bubblesort(A):
	for i in range(0,len(A)-1):
		for j in range(0,len(A)-i-1):
			if A[j]>A[j+1]:
				A[j],A[j+1]=A[j+1],A[j]
	return A
x = [r.randint(0,1000) for y in range(0,500)]
s = t.time()
print(x[:25])
print("Sorting..")
x = bubblesort(x)
print(x[:25])
print("Time taken = ",t.time()-s)