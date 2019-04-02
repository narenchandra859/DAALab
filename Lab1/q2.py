import random as r
import time as t
def selsort(A):
    for i in range(0,len(A)):
        m=i
        for j in range(i,len(A)):
            if(A[m]>A[j]):
                m=j
        A[i],A[m]=A[m],A[i]
    return(A)
n=int(input("Enter the max range of elements : "))
s=t.time()
x=[r.randint(0,50000) for i in range(n)]
x=selsort(x)
f=t.time()
print(x)
print("Sorted",n,"random elements from 0->50000, It took",f-s,"seconds")
