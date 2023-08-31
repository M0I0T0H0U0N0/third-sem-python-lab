#Suppose that a text file contains marks for 6 courses
#for a student in a line. Each course marks is separated
#by space as delimiter. File contains marks for ‘n’
#number of students in separate lines. Write a program
#that reads the marks from the file for each student and
#displays the total and average. Your program should
#prompt the user to enter a filename.


file_name = input("enter a file name")
try:
	with open(file_name,'r') as file:
		total = 0
		for line in file:
			marks = line.split()
			print(marks)
			for mark in range(0,len(marks)):
				total = total + int(marks[mark])
				Average = total / len(marks)
			print("total marks = ", total,"Average marks=%.3f " %Average)
except FileNotFoundError:
	print("file not found")
