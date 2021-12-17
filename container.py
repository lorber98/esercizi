print("---------------------------------")
v=[]									# empty list instance
print(v)
m=["Lista","di",4,"elementi"]
print(m[2],m[0])						# access single list elements
print("---------------------------------")


print("Slicing operator")
a=[0,1,2,3,4,5,6,7]
print(a)
print(a[0:6])
print(a[1:6:2])
print(a[1::2])				# no ‘stop’ means until the end of list
print(a[::2])				# no ‘start’ means from the first item of the list
print(a[6:0:-2])			# starts fom index 6, ends to index 0 going back with step 2
print("---------------------------------")

#-------------------------------------------
print("Range()")
"""x = range(6)
for n in x:
  print(n)
print(x)"""

b=range(3)
print(b)
print(type(b))

c=list(range(1,10))
print(c)
print(type(c))

d=list(range(1,10,2))
print(d)
print("---------------------------------")
#-------------------------------------------

#-------------------------------------------
print("Complex operations")
d=list(range(10))
d2=[el*2 for el in d]
print("d=",d)
print("d2=",d2)

l=[1,2]
l2=['a','b']
l3=[4,5]
f=[(e1,e2,e3) for e1 in l for e2 in l2 for e3 in l3]
print(f)
print("---------------------------------")
for e1 in l:
	for e2 in l2:
		for e3 in l3:
			f.append((e1,e2,e3))
print("Con for, f=",f)
print("---------------------------------")

#-------------------------------------------
print("---------------------------------")
print("---------------------------------")
print("---------------------------------")
