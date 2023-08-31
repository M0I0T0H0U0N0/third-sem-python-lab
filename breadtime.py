#Write an Object oriented Python program to create two Time objects: currentTime,
#which contains the current time; and breadTime, which contains the amount of time it takes
#for a bread maker to make bread. Then we'll use addTime to figure out when the bread will
#be done. Write the printTime function to display the time when the bread will be done by
#the bread maker.





class Time:
	def __init__(self, hour, minute, second):
		self.hour = hour
		self.minute = minute
		self.second = second
print("Enter the current time")
currenthour = int(input("Hour: "))
currentminute = int(input("Minute: "))
currentsecond = int(input("Second: "))
currentTime = Time(currenthour, currentminute, currentsecond)
print("Enter the time required to make bread")
breadhour = int(input("Hour: "))
breadminute = int(input("Minute: "))
breadsecond = int(input("Second: "))
breadTime = Time(breadhour, breadminute, breadsecond)
finishHour = 0
finishMinute = 0
finishSecond = 0
def addTime():
	global finishHour
	finishHour = currentTime.hour + breadTime.hour
	global finishMinute
	finishMinute = currentTime.minute + breadTime.minute
	global finishSecond
	finishSecond = currentTime.second + breadTime.second
	if finishSecond > 60:
		finishMinute = finishMinute + 1
		finishSecond = finishSecond % 60
	if finishMinute > 60:
		finishHour = finishHour + 1
		finishMinute = finishMinute % 60
	if finishHour > 12:
		finishHour = finishHour % 12
def printTime():
	tempHour = ""
	tempMinute = ""
	tempSecond = ""
	if len(str(finishHour)) == 1:
		tempHour = "0" + str(finishHour)
	else:
		tempHour = str(finishHour)
	if len(str(finishMinute)) == 1:
		tempMinute = "0" + str(finishMinute)
	else:
		tempMinute = str(finishMinute)
	if len(str(finishSecond)) == 1:
		tempSecond = "0" + str(finishSecond)
	else:
		tempSecond = str(finishSecond)
	print("The bread will be done at:", tempHour + ":" + tempMinute + ":" + tempSecond)
addTime()
printTime()
