#Write a program that will count the number of characters, words,and lines in a file.
#Words are separated by a white-space character. Your program should prompt the userto
#enter a filename.


str1 = input("enter a file name")
with open(str1, 'r') as f:
	nl = nw = nc = 0
	list1 =[]
	for line in f:
		nl = nl + 1
		words = line.split()
		# list1.extend(words)
		# print(list1)
		nw = nw + len(words)
		for i in words:
			nc =nc + len(i)
print("Number of lines in program ",nl," Number of words in file",nw,"number of character",nc)
