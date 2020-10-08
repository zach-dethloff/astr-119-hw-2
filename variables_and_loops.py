import numpy as np 

def main():
	i = 0  #declaring integers to count over for our loops
	n = 8
	x = 300.0 #proposing a float for mathematical operations
	z = np.zeros(n,dtype=float) #np creates an array of 8 zeros

	for i in range(n):
		z[i] = 3.0 * float(i) + 4 #setting the index of z based on i's value to a different value, ie not zero

	for z_element in z: #printing out each element in the z variable
		print(z_element)


if __name__ == '__main__': #running the main function
		main()	
