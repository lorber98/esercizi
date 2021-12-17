print("---------------------------------")
# Prova break con WHILE

number = 23
running = True

while running:
	guess = int(input('Enter an integer : '))
	if(guess==number):
		print(number)
		break
	else:
		print("Try again")
else:
	print("L'else viene eseguito)")
print("---------------------------------")
# Senza Break
number = 23
running = True

while running:
	guess = int(input('Enter an integer : '))
	if(guess==number):
		print(number)
		running = False
	else:
		print("Try again")
else:
	print("L'else viene eseguito")
print("---------------------------------")

# ------------------------------------------------------------------------------------------------------------
# analogamente con FOR

print("---------------------------------")
# Prova break con FOR
for i in range(1, 5):
	print(i)
	break
else:
	print("L'else viene eseguito")
print("---------------------------------")

print("---------------------------------")
# Prova senza break con FOR
for i in range(1, 5):
	print(i)
else:
	print("L'else viene eseguito")
print("---------------------------------")
