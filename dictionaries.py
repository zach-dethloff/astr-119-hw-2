practice_dict = { #creating a dictionary with keys and indeces
	"work" : "Homework",
	"user" : "Zach",
	"hunger" : 6
}

print(type(practice_dict)) #displaying dtype of dictionary

assignment = practice_dict["work"]
print(assignment) #using a key to get dictionary data and printing it

practice_dict["hunger"] += 2 #adding value to dictionary value

print(practice_dict)

for z in practice_dict.keys(): #running through each key and printing it as well as 
	print(z, practice_dict[z]) #its index counterpart