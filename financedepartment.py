#The finance department of a company wants to calculate the monthly pay of one of its
#employee. Monthly pay should be calculated as mentioned in the formula below and display
#all the employee details. Monthly Pay= No. of hours worked in a week * Pay rate per hour *
#No .of weeks in a Month. Write a function in Python Program to implement the problem.




def Salary_calculation():
	name = input("enter your name")
	hrs_worked = int(input("enter number of hours worked"))
	No_of_weeks = int(input("enter number of weeks worked"))
	pay_hr = float(input("enter pay per hour "))
	month_salry = hrs_worked * No_of_weeks * pay_hr
	print("name of an employee", name)
	print("hours worked \n", hrs_worked)
	print("no of weeks worked \n", No_of_weeks)
	print("pay per hpur \n", pay_hr)
	print("mpntly saalry \n", month_salry)
Salary_calculation()
