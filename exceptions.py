try:
	print(z) #attempting to print an undefined variable
except:
	print("z does not have a definition!") #creating an exception for the problem

try:
	print(z)
except NameError:
	print("z is still not defined") #printing out a specific message for a specific error
except:
	("something unexpected happened")

print(z) #this will give us a default python error