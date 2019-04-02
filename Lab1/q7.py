import random as r
import time as t
def merge(A,B):
    i,j,l=0,0,[]
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            l.append(A[i])
            i=i+1
        else:
            l.append(B[j])
            j=j+1
    if i<len(A):
        for x in range(i,len(A)):
            l.append(A[x])
    else:
        for x in range(j,len(B)):
            l.append(B[x])
    return(l)
def mergesort(A):
    n=len(A)
    if n==1:
        return(A)
    B=A[:(n//2)]
    C=A[(n//2):]
    B=mergesort(B)
    C=mergesort(C)
    A=merge(B,C)
    return(A)
n=int(input("Enter the upper limit of range of numbers : "))
s=t.time()
x=[r.randint(0,50000)for i in range(n)]
x=mergesort(x)
f=t.time()
print("Sorted",n,"random numbers between 0->50000. It took",f-s,"seconds.")
