tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])				# access to single element
print("tup2[1:5]: ", tup2[1:5]) 		# access to slice

"""del tup1
print("After deleting tup1: ")
print(tup1)"""
print("---------------------------------")
print((tup1)*2)
print(len(tup1))
print(tup1+tup2)
print(1997 in tup1)
#for x in tup2: print(x)
print(max(tup2))
print("---------------------------------")
d=list(range(6))
print(d, " - ", type(d))
d_tup = tuple(d)
print(d_tup, " - ", type(d_tup))

