import time as t
import random as r
def mergeSort(l):
	n = len(l)
	if n == 1:
		return l
	A = l[:n//2]
	B = l[n//2:]
	A = mergeSort(A)
	B = mergeSort(B)
	C = merge(A,B)
	return C

def merge(A,B):
	global count
	i, j, m = 0, 0, []
	while i<len(A) and j<len(B):
		if A[i]<B[j]:
			m.append(A[i])
			i = i + 1
		else:
			m.append(B[j])
			count = count + len(A[i:])
			j = j + 1
	if i == len(A):
		for x in range(j,len(B)):
			m.append(B[x])
	else:
		for x in range(i,len(A)):
			m.append(A[x])
	return m
count = 0
#x = [r.randint(0,10000) for y in range(100)]
x = [5,4,2,1,7,10,3,11,14,15]
print(x[:])
s = t.time()
print("Sorting..")
x = mergeSort(x)
print(x[:])
print("Time taken = ",t.time()-s)
print("Inversions = ",count)
