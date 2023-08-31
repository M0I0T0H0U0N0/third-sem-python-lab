#Write a program to remove all punctuations like “’! ()-[]{};:’’’,\,<>,/,?,@,#,$,%^&*_~”from
#the string provided by the user.

str1 = input("enter a string")
result = " "
for char in str1:
	if char not in " '' \"" "! ()-[]{};:’’’,\,<>,/,?,@,#,$,%^&*_ " :
		result += char
print(result)
