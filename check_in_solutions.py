def main(): #this will be the definition for the main function
	i = 0
	x = 400.0
	for i in range(401): #looping i variable from 0 to 400
		if((i%2)==0): #checking to see if i is even
			x += 10  # adding 10 if it is even
		else: #if i is odd option
			x -= 14 # subtracting 14 if i is odd

	y = "%3.2e" % x #turning final output into a string containing x in sci. notation
	print(y) #printing y output to the screem

if __name__ == "__main__": #running the actual function
	main()

