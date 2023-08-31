#Design a class named Rectangle to represent a rectangle. class contains:Two data fields
#named width and height.
#A constructor that creates a rectangle with the specified width and height. A method named
#getArea() that returns the area of this rectangle.


class Rectangle:
	def __init__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		return (self.l * self. b)
n =int(input(" Enter the number of rectangle"))
list1 = []
list_area = []
for i in range(0,n):
	w = float(input("Enter the width of rectangle%d" % (i + 1)))
	h = float(input("Enter the height of rectangle%d" % (i + 1)))
	list1.append(Rectangle(w, h))
	list_area.append(list1[i].area())
	print(list1[i].l)
	print(list1[i].b)
i_of_max = list_area.index(max(list_area))
i_of_min = list_area.index(min(list_area))
print("Width and list1[i_of_max].b)heightofrectanglehavingmaximumarea",list1[i_of_max].l,list1[i_of_max].b)
print("Width and list1[i_of_min].b)heightofrectanglehavingminimumarea",list1[i_of_min].l,list1[i_of_min].b)
