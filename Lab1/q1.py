import time as t
def binsearch(A,h,l,se):
    mid=(h+l)//2
    if(h<l):
        return -1
    if(se==A[mid]):
        return mid
    elif(se>A[mid]):
        return binsearch(A,h,mid+1,se)
    elif(se<A[mid]):
        return binsearch(A,mid-1,l,se)
n=int(input("Enter the searching element "))
m=int(input("Enter the maximum range of elements "))
s=t.time()
x=[int(a) for a in range(m)]
pos=binsearch(x,len(x)-1,0,n)
f=t.time()
print("Element was found at position",pos,"It took",f-s,"seconds.")
