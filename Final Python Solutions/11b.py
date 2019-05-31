def knapsack(n,w):
    M=[[0 for i in range(w+1)]for i in range(len(item))]
    for i in range(1,len(item)):
        for j in range(1,w+1):
            if(item[i][0]>j):
                M[i][j]=M[i-1][j]
            else:
                M[i][j]=max(M[i-1][j],item[i][1]+M[i-1][j-item[i][0]])
    subset=[]
    i,j=n,w
    while i>=0 and j>=0:
        if M[i-1][j]<M[i][j]:
            subset.append(i)
            j=j-item[i][0]
            i=i-1
        else:
            i=i-1
    print(M, item)
    return(M[-1][-1],subset)

n=int(input("Enter number of items : "))
item=[0]
for i in range(n):
    w=[int(x) for x in input("Enter wt, value of item: ").split()]
    item.append(w)
w=int(input("Enter maximum wt: "))
mw,sub=knapsack(n,w)
print("max=",mw)
print("sol=",sub)