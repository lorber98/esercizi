import numpy as np

#----------------------------------------------
print("Example slide 36")
c = np.arange(1,5)
d = np.array([[1,1,1,1],[10,10,10,10]])
print("Array c =", c)
print("Array d =", d)
print ("c + d =",c+d)
print("---------------------------------------------------")

#----------------------------------------------
print("Example 1: slide 37")
a=np.array([1,2,3])
print("a:",a)
print("a.shape: ",a.shape)						# (3,)
b=np.array([[1,2,3],[4,5,6]])
print("b:",b)
print("b.shape:",b.shape) 						#(2,3)
c=a+b
print("a+b=",c)
print("---------------------------------------------------")


#----------------------------------------------
print("Example 2: slide 37")
a=np.arange(6)
a=a.reshape((2,1,3))
b=np.arange(8)
b=b.reshape((2,4,1))
c=a+b
print("---------------------------------------------------")

#----------------------------------------------
print("Example 3: slide 37")
a=np.arange(30)
a=a.reshape((2,5,3))
b=np.arange(8)
b=b.reshape((2,4,1))
c=a+b
print("---------------------------------------------------")





