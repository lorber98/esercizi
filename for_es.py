print("---------------------------------")
a=[1,2,3,4,5]
for el in a:
	print(el)
print("---------------------------------")
a="Ciao"
for el in a:
	print(el)
print("---------------------------------")
b=set([1,2,3,4])
for el in b:
	print(el)
print("---------------------------------")


print("---------------------------------")
d={1:"a", 2:"b"}
for el in d.keys():
	print(el)
print("_____")
for el in d.values():
	print(el)
print("_____")
for el in d:
	print(el)
print("_____")
for k,v in d.items():
	print(k,v)
print("_____")

g={1:"a", 2:"b", 4:"d", 3:"c"}
for el in (1,2,3):
	print(g.get(el))
print("---------------------------------")
print("---------------------------------")
print("---------------------------------")
