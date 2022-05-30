import csv

file = open('employees.csv')
group_A = []
name_employee = []
lastname = []
salary = []


try:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if row[3] == "Manager":
            group_A.append(float(row[2]))
            # it will add salary of all managers to the list
        if csv_reader.line_num > 1:
            salary.append(float(row[2]))
            # adds salary of all employees into a list
            name_employee.append(row[0])
            # adds first name of all employees into a list
            lastname.append(row[1])
            # adds last name of all employees into a list

finally:
    file.close()

avg = sum(group_A)/len(group_A)
print("Average salary of Managers", int(avg))
lowest = min(salary)
index = salary.index(lowest)
Firstname = name_employee[index]
last_name = lastname[index]
print(Firstname, last_name, "has the lowest salary")
