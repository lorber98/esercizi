import numpy as np

a=np.array([[1,2,3],[8,8,8]])
print("a =",a)
print("a.shape =",a.shape)
print("Dimensione a =",a.ndim)

b=np.array([[1,2],[3,4],[5,6],[7,8]])
print("Array b")
print(b)
print("b.shape =",b.shape)
print("Dimensione b =",b.ndim)
print("---------------------------------------------------")


c = np.array([1,2,3,4])
print(c, "\n --- ---")
list1 = [1,2,3,4]
tupla = (5,6,7,8)
d = np.array(list1)
e = np.array(tupla)
f = np.array([list1,tupla])
print(d, "\n --- ---")
print(e, "\n --- ---")
print(f, "\n --- ---")
print("---------------------------------------------------")


print("Array from a string")
print(np.fromstring('1 2', dtype=int, sep=' '))
print(np.fromstring('1, 2', dtype=int, sep=','))




