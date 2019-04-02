def menEngaged(L):
    if 0 in L.values():
        return 1
    else:
        return 0
def ChooseMan(L):
    for k, v in sorted(L.items()):
        if v==0:
            return k
def propose(M,W,mP,wP,a):
    a=a-1
    for x in range(0,len(M)):
        j=M[a][x]
        if(wP[j]==0):
            wP[j]=a+1
            mP[a+1]=j
            break
        else:
            k=wP[j]
            v1=W[j-1].index(k)
            v2=W[j-1].index(a+1)
            if(v1<v2):
                continue
            else:
                wP[j]=a+1
                mP[a+1]=j
                mP[k]=0
                break
n=int(input("Enter the number of men/women : "))
print("Enter MENS pref list : ")
M=[[int(x) for x in input().split()]for y in range(n)]
print("Enter WOMENS pref list : ")
W=[[int(x) for x in input().split()]for y in range(n)]
mP,wP={},{}
for i in range(1,n+1):
    mP[i],wP[i]=0,0
while(menEngaged(mP)):
    a=ChooseMan(mP)
    propose(M,W,mP,wP,a)
for k, v in sorted(wP.items()):
    print("Man",k,"engaged to Woman",v)

