#Write a program to count the number of capital letters and display the position of each
#capital letter in a user entered string via keyboard.


str1 = input("enter a string")
list1 = []
list2 = []
for i in range(0, len(str1)):
	if str1[i].isupper():
		list1.append(str1[i])
		list2.append(i)
	print("number of capital letter" , len(list1))
	print("capitalletter position")
for i in range(0, len(list1)):
	print(list1[i],"   ", list2[i])
