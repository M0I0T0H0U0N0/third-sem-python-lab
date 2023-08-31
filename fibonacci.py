#Write a Python program to generate first ‘n ’Fibonacci numbers.


fib1 = 0
fib2 = 1
n = int(input("enter the no"))
if n == 0 :
	print(f"invalid Input")
if n == 1:
	print(fib1)
if n > 1:
	print(fib1)
	print(fib2)
	for i in range(2, n):
		fib3 = fib1 + fib2
		print(fib3)
		fib1 = fib2
		fib2 = fib3
