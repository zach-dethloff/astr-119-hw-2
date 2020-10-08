z = [1.0, 4.0, 8.0, 2.2, 4.5] #create an array
print(type(z))

x = z.pop(3) #removing the 4th element
print(z)
print(x)

z.remove(4.0) #removing the 4.0 value from the list
print(z)

z.append(3.6) #adding an element at the end
print(z)

y = z.copy() #copying the z array
print(y)

print(y.count(4.5)) #counting how many times 4.5 is present in the array

print(y.index(1.0)) #printing the index number of the 1.0 value

y.sort() #sorting values of the array
print(y)

y.reverse() #reversing current array order
print(y)

z.clear() #clearing entire z array
print(z)