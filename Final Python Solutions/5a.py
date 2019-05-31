import time as t
print("Enter 'c1' and 'c2' values for the function ( c1*g(n) <= f(n) <= c2*g(n) ): ")
x = [int(a) for a in input().split()]
c1 = x[0]
c2 = x[1]
print("Finding n0 value..")
n0 = 0
s = t.time()
i = 0
while(1):
	i = i + 1
	fn = 7*i*i + 7*i + 5
	gn = c1*i*i
	gn1 = c2*i*i
	if gn <= fn and fn <= gn1:
		print("'n0' value is found to be",i)
		n0 = i
		break
print("Function Values Table : ")
print("F(n)\tc1*G(n)\tc2*G(n)")
for x in range(1,i+1):
	fn = 7*x*x + 7*x + 5
	gn = c1*x*x
	gn1 = c2*x*x
	print(fn,"\t",gn,"\t",gn1, sep="")
print("Time taken = ",t.time()-s)