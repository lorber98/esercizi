import math

r=12+5j
a=5
b=2


print(r, type(r))
print("Parte reale:",r.real,type(r.real))
print("Parte immaginaria:",r.imag, type(r.imag))
print("---------------------------------")
print(a, type(a))
print(b, type(b))
print("---------------------------------")
for i in range(0,5,1):
	print("i=",i)
	if (i == b and a<10):
		print("Find b:",i)
print("---------------------------------")
print("sin(b)=",math.sin(a))
print("---------------------------------")

