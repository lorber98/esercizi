import numpy as np

b = np.array([5,6,7,8])
c = np.arange(1,5)
d = c + b
print("Sum",b,"+",c,"=",b+c)
b += 1
print("Autoincrement b +=1, b =", b)
print("Multiply c*3",c,"* 3 =",c*3)
print("Sin (c) =", np.sin(c))
print("---------------------------------------------------")

#-------------------------------------------------------------------------
#Product vector-matrices
v1 = np.array([1,2,3])
v2 = np.array([10,20,30])
print(v1,"\n --- ---\n",v2,"\n --- ---")
print(v1*v2)
print("---------------------------------------------------")
print("Scalar product v1.v2: ",np.dot(v1,v2))
print("---------------------------------------------------")


#-------------------------------------------------------------------------
#product between matrices
m1=np.matrix(v1)
m2=np.matrix(v2)
print(m1,"\n --- ---")
print(m2,"\n --- ---")
print("shape m1:", m1.shape, "- shape m2:", m2.shape)

try:
	m1*m2 #ERRORE
except Exception as err:
	print(err)
	
#Re-define m2 as column vector:
m2=np.matrix(v2[:,np.newaxis])
print("Product: ",m1*m2)
print("---------------------------------------------------")








