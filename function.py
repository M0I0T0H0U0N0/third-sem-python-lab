#Write a function that returns the index of the smallest element in a list of
#integers. If the number of such elements is greater than 1,return the smallest
#index. Use the following header:
#def indexOfSmallestElement(lst):
#Write a test program that prompts the user to enter a list of numbers, invokes this
#function to return the index of the smallest element and displays the index.



def IndexOfSmallestElement(list1):
	t = min(list1)
	return list1.index(t)
list1=[]
n = int(input("Enter the number of elements in a list"))
for i in range(0, n):
	list1.append(int(input("enter a element")))
index = IndexOfSmallestElement(list1)
print("Index of smallest element in am list is %d" %(index+1))
