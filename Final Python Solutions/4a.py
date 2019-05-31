import time as t
c = int(input("Enter the 'c' value for the function : "))
print("Finding n0 value..")
n0 = 0
s = t.time()
i = 0
while(1):
	i = i + 1
	fn = 3*i*i + 4*i + 3
	gn = c*i
	if gn < fn:
		print("'n0' value is found to be",i)
		n0 = i
		break
print("Function Values Table : ")
print("F(n)\tc*G(n)")
for x in range(1,i):
	fn = 3*x*x + 4*x + 3
	gn = c*x
	print(fn,"\t",gn, sep="")
print("Time taken = ",t.time()-s)