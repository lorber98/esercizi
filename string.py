var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])
print("---------------------------------")

a = """I am a string spanning in 3 rows,
containing 'sigle quotes',
containing "double quotes",
containing '''triple quotes''' """
print(a)
print("---------------------------------")

a = 'He'+'l'*2+'o World'
print(a)
print("---------------------------------")

name = "Peter"
my_string = "Hello %s" % name 							# Append or insert
print(my_string)
my_string = "Hello %s, how are you? %s" % (name, 'ok')	# Insert multiple values
print(my_string)
print("---------------------------------")


b = 'Hello \t World'
print(b)
b = r'Hello \t World'		#r or R to not "print" a tab but only "\t"
print(b)
print("---------------------------------")


#esempio pag. 26
c = "Oggi è %s %d %s" % ("Venerdì",20,"Febbraio")
print(c)
print("---------------------------------")

person = {"name": "John", "age": 50}
person = {"name": "Taylor", "age": 22}
print(f"{person['name']} is {person['age']} years old.")
print("{person['name']} is {person['age']} years old.")		#senza f-string
print("---------------------------------")

print("---------------------------------")

print("---------------------------------")



