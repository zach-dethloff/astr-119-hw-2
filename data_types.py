import numpy as np #importing libraries

n = 12 #creating an integer
print(type(n)) #prints the type of data contained by variable n

a_n = np.zeros(n,dtype=int) #creating an array of zeros classified as integers
print(type(a_n)) #printing out array type
print(type(a_n[0])) #printing out the type of a specific array index

z = 200.0 #new variable presented as a float
print(type(z)) #print dtype as float

i = 2.22e2 #float but in sci notation
print(type(i))

m = np.zeros(n,dtype=float) #creating a new arrays of zeros as floats not ints
print(type(m)) #dtype of array
print(type(m[0])) #dtype of index in array