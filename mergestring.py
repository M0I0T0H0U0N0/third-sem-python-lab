#Consider two strings, String1 and String2 and display the merged string as output. The
#merged string should be the capital letters from both the strings in the order they appear.
#Sample Input:
#String1:ILikeC
#String2:MaryLikesPythonS
#Merged string should be ILCMLPS




str1 = input("enter a string1")
str2 = input("enter a second string")
str3 = ""
for i in range(0,len(str1)):
	if str1[i].isupper():
		str3 += str1[i]
for i in range(0,len(str2)):
	if str2[i].isupper():
		str3 += str2[i]
print(" Resultant String is", str3)
