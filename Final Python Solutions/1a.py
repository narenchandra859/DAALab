# Recursive Binary Search
# O(log n)
import time as t
import random as r
def bsearch(l, high, low, ele):
  if(low<=high):
    mid = (low+high)//2
    if ele == l[mid]:
      return l.index(ele)
    elif ele > l[mid]:
      return bsearch(l, high, mid+1, ele)
    elif ele < l[mid]:
      return bsearch(l,mid-1, low, ele)
  else:
    return -1
x=[r.randint(0,501) for y in range(1000000)]
s = t.time()
x.sort()
print(bsearch(x,len(x),0,500))
f = t.time()
print("Time = ",f-s)