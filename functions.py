import numpy as np #importing libraries
import sys

def get_num(z): #generating an exponential with numpy functions
	return np.exp(z) #returning the number to the function

def show_get_num(n): #subroutine to output get_num values
	for m in range(n):
		print(get_num(float(m))) #calling get_num and printing values

def main(): #main function
	n = 0 #proposing a default variable to change and use for looping

	if(len(sys.argv)>1): #looks for input argument on command line
		n = int(sys.argv[1]) #sets value of n to that value

	show_get_num(n) #runs subroutine

if __name__ == '__main__': #runs main function
	main()