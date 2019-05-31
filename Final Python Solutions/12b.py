def compute_M():
    M.append(0)
    for i in range(1,len(job)):
        M.append(max(M[i-1],job[i][2]+M[P[i]]))

def find_sol(j):
    if j>0:
        if(job[j][2]+M[P[j]]>=M[j-1]):
            S.append(j)
            find_sol(P[j])
        else:
            find_sol(j-1)

def compute_pred():
    P.append(0)
    for i in range(1,len(job)):
        for j in range(i-1,-1,-1):
            if job[j][1]<=job[i][0]:
                P.append(j)
                break


job,S,M,P=[],[],[],[]
job.append([0,0,0])
n=int(input("Enter number of jobs : "))
for i in range(n):
    #print("Enter the start, finish and value of job : ")
    x=[int(a) for a in input().split()]
    job.append([x[0],x[1],x[2]])
job.sort(key=lambda x:x[1])
compute_pred()
compute_M()
find_sol(n)
print("Jobs chosen = ",S)
print("Max = ",M[-1])