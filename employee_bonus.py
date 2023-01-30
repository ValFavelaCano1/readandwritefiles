import csv

infile = open("EmployeePay.csv", "r")

employees = csv.reader(infile, delimiter=",")

next(employees)

for row in employees:
    Employee_ID = row[0]
    First_Name = row[1]
    Last_Name = row[2]
    Salary = int(row[3])
    Bonus = float(row[4])

    calculated_bonus = Salary * Bonus
    total_income = Salary + calculated_bonus

    print("Employee ID:   ", Employee_ID)
    print("Full Name:     ", First_Name, Last_Name)
    print("Salary:        ", "$", format(Salary, ">4,.2f"))
    print("Bonus:        ", " $", format(calculated_bonus, ">4,.2f"))
    print("Total Income:  ", "$", format(total_income, ">4,.2f"))
    print()

infile.close()
