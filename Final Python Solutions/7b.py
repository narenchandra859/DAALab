def quicksort(A, low, high):
	if low < high:
		pivot = A[high]
		i = low - 1
		for n in range(low,high):
			if A[n] <= pivot:
				i = i + 1
				A[n], A[i] = A[i], A[n]
		A[i+1], A[high] = A[high], A[i+1]
		quicksort(A,low,i-1)
		quicksort(A,i+1,high)
		return(A)
l = [5,4,2,1,7,10,3,11,14,15]
print(quicksort(l,0,len(l)-1))


