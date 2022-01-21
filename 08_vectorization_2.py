def func_NumPy(x):
	r = x.copy() # allocate result array
	for i in range(np.size(x)):
		if x[i] < 0:
			r[i] = 0.0
		else:
			r[i] = sin(x[i])
	return r
	

