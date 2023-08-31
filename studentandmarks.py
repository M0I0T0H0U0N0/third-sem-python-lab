#Develop python program to perform the below mentioned operations.
#a) display total marks scored by each student
#b) Display top scorer and the top score
#Scenario: There are 8 students and answers t o 10 multiple choice questions of each
#student is stored in a file called marks.txt. Each answer is delimited by space. Each line
#provides a student’s answers to the questions, as shown below.The answer key isstored in
#a file named keys.txt. The format of answer keys as shown below.





key = open("key.txt", 'r').readline().split()
mark = open("mark.txt", 'r')
top = 0
x=0
#name_list =[]
mark_list = []
for line in mark:
	t = line.split()
	nm = t[0]
	#name_list.append(nm)
	count = 0
	for i in range(1,len(key) + 1):
		if t[i] == key[i - 1]:
			count = count + 1
print(nm,"scored ",count,"/10")
mark_list.append(count)
top = max(mark_list)
x = mark_list.index(top)
print("student%d is a top scorer%d/10" %(x+1,top))
