import numpy as np

a = np.arange(20)
print(a)
print("a shape:", a.shape,"\n *** ***")
a.resize(5,6)
b=a
print(b)
print("b shape:", b.shape,"\n *** ***")
print("---------------------------------------------------")


#-------------------------------------------------------------------------
c=np.array(range(1,9))
print("C-style re-shaping") 
print( c.reshape((2,2,2),order='C') ) 		# Array Method: C Style)

print("F-style re-shaping")
print( c.reshape((2,2,2),order='F') ) 		# Array Method: Fortran Style
print("---------------------------------------------------")

#-------------------------------------------------------------------------
#d = np.arange(5,10)
d= np.ones(4)
e = np.arange(1,5)
print(d,"\n *** ***")
print(e,"\n *** ***")
d += e
print(d,"\n *** ***")
print("d[0] =", d[0])
d[1:3]=d[1:3]*3 		# Modify the elements from 1 to 3
print(d, "\n *** ***")
print("---------------------------------------------------")


#-------------------------------------------------------------------------
a1 = np.arange(25)
print(a1,"\n *** ***")
a1 = a1.reshape((5,5))
print(a1)
print("---------------------------------------------------")

#-------------------------------------------------------------------------
# Copy
c = a1.copy()
print("id(a):", id(a), "id(c):", id(c))
c[0]=122
print("c=\n" , c , "\n *** *** \na", a1)
print("---------------------------------------------------")


#-------------------------------------------------------------------------
# Copy 2
a2 = np.arange(5)
b2 = np.zeros_like(a2) # Return an array of zeros with the same shape and type as a given array.
b2[:] = a2[:]

# Copy is element-by-element and the two objects are different
b2[3] = 1000
b2 == a2
print(a2, "\n *** ***")
print(b2, "\n *** ***")














