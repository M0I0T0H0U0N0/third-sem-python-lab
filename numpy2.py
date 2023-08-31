#Write a NumPy program to create a random array with 1000 elements and compute
#the average, variance, standard deviation of the array elements



import numpy as np
x = np.random.randn(1000)
print("Average of the array elements:")
mean = x.mean()
print(mean)
print("Standard deviation of the array elements:")
std = x.std()
print(std)
print("Variance of the array elements:")
var = x.var()
print(var)
