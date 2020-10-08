def ifelse_control(z): #creating a function
	if(z==6): #checking to see if z = 6
		b = "Variable z = %d equals 6." % z #output string for z = 6
	elif(z==3):
		b = "Variable z = %d equals 3." % z #string if z = 3
	else:
		b = "Variable z = %d doesn not equal 3 or 6." % z #last scenario string output

	print(b) #printing the chose string

def main():
	n = 0 #creating a useful integer
	ifelse_control(n) #using the function when n=0
	n=1
	ifelse_control(n) #using function when n=1
	n=6
	ifelse_control(n) #using the function when n doesnt equal 1 or 0

if __name__ == '__main__': #main run command
		main()	


