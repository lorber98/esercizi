import numpy as np

a=np.arange(0,4*np.pi,0.1)

#VECTORIZED VERSION
y=np.sin(a)*2
print(y)
print(" --- ---")
#SCALAR VERSION
y=np.zeros(len(a))
for i in range(len(a)):
	y[i]=np.sin(a[i])*2
print(y)
