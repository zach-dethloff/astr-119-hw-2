s = "This is a string" #declaring a string
print(type(s)) #printing dtype of s

no = True
print(type(no)) #printing the dtype of a boolean (True)

yes = False
print(type(yes)) #printing dtype of a False boolean

zeta_list = ["x", "y", "z"] #creating a list object
print(type(zeta_list)) #printing dtype of list
print(type(zeta_list[0])) #printing dtype of list elements
zeta_list.append("w") #adding a list element
print(zeta_list) #prints new list

zeta_tuple = ("x", "y", "z") #creates an immutable tuple
print(type(zeta_tuple)) #dtype of tuple

try: #attempt at running a command
	zeta_tuple[2] = "w" #attempt at changing an index value
except TypeError:
	print("Can't mess with tuples once they are made") #output for inevitable error
print(zeta_tuple) #printing out tuple

