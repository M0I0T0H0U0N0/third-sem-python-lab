#Write a binary search function which searches an item in a sorted list. Thefunction should
#return the index of element to be searched in the list.

def binary_search(list1, key, n):
	low = 0
	high = n-1
	while low <= high:
		mid = int((low + high) / 2)
		if list1[mid] == key:
			return mid
		elif list1[mid] > key:
			high = mid - 1
		else:
			low = mid + 1
	return -1
list2 = []
n1 = int(input("enter a total number in a list"))
for i in range(0, n1):
	value = int(input("enter a item of a list"))
	list2.append(value)
	list2.sort()
	print(list2)
key1 = int(input("enter a key value to be searched"))
index = binary_search(list2, key1, n1)
if index == -1:
	print("Un successful search")
else:
	print("element is found in %d position" %(index+1))
