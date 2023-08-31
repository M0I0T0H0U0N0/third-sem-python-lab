#The finance department wants to calculate the monthly net pay of one of its employee by
#finding the income tax to be paid and the net salary after the income tax deduction. The
#employee should pay the income tax based on the following table: Display basic salary,
#allowances, gross pay, income tax and net pay

emp_id = int(input("enter a employee id"))
allowance = float(input("enter employee allowance"))
basic_Salary = float(input("enter employee salry"))
Gross_Salary = basic_Salary + allowance
if Gross_Salary > 20000:
	tax = Gross_Salary * 0.3
elif Gross_Salary > 10000 :
	tax = Gross_Salary * 0.2
elif Gross_Salary > 5000:
	tax = Gross_Salary * 0.1
else:
	pass	
	
Net_salary = Gross_Salary - tax
print("employee id\n ", emp_id)
print("Salary Of an Employee\n", basic_Salary)
print("Allowance of an Employee\n", allowance)
print("employees Total Salary\n", Gross_Salary)
print("Tax paid by Employee\n", tax)
print("Toatal Salary Aftwer tax dedcuction",Net_salary)
