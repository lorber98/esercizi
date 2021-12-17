my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name']) 					# Output: Jack
print(my_dict.get('age')) 				# Output: 26



print("---------------------------------")
# update value
my_dict['age'] = 27
print(my_dict)
# add item
my_dict['address'] = 'Downtown'
print(my_dict)
print("---------------------------------")



print("---------------------------------")
squares = {1:1, 2:4, 3:9, 4:16, 5:25}	# create a dictionary

print(squares.pop(4))					# remove a particular item
print(squares)
print("_________________________________")
print(squares.popitem())				# remove an arbitrary item
print(squares)
print("_________________________________")
"""#del squares[5]							# delete a particular item
#print(squares)
print("_________________________________")

squares.clear()							# remove all items
print(squares) 							# Output: {}
print("_________________________________")
#del squares								# delete the dictionary itself
#print(squares)							# Throws Error"""
print("---------------------------------")



print("---------------------------------")
squares_2 = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(len(squares_2))
print(sorted(squares_2))
print("---------------------------------")
