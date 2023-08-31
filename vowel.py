#Write a program to count the number of each vowel in a given string.



str1 = input("enter the string")
str2 = str1.lower()
count = 0
dict1 = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for i in range(0,len(str1)):
	if (str2[i] == 'a' or str2[i] == 'e' or str2[i] == 'i'or str2[i] == 'o'or str2[i]=='u'):
		dict1[str2[i]]+= 1
		count += 1
print(dict1)
print("no of vowels = ", count)
