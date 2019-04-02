import random as r
import time as t
def inssort(A):
    for i in range(1,len(A)):
        pos=i
        while pos>0 and (A[pos]<A[pos-1]):
            A[pos],A[pos-1]=A[pos-1],A[pos]
            pos=pos-1
    return(A)
n=int(input("Enter the upper limit of range of numbers : "))
s=t.time()
x=[r.randint(0,50000) for i in range(n)]
x=inssort(x)
f=t.time()
print("Sorted",n,"random numbers from 0->50000. It took",f-s,"seconds")
