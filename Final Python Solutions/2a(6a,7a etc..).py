import time as t
c = int(input("Enter the 'c' value for the function : "))
print("Finding n0 value..")
n0 = 0
s = t.time()
for i in range(1,31):
	fn = 7*i + 5
	gn = c*i
	if gn > fn:
		print("'n0' value is found to be",i)
		n0 = i
		break
print("Function Values Table : ")
print("F(n)\tc*G(n)")
for i in range(1,31):
	fn = 7*i + 5
	gn = c*i
	print(fn,"\t",gn, sep="")
print("Time taken = ",t.time()-s)