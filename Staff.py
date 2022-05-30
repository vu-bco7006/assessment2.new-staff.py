import csv

file = open('employees.csv')
group_A = []

try:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        if row[3] == "Manager":
            group_A.append(float(row[2]))
            # it will add salary of all managers to the list

finally:
    file.close()

avg = sum(group_A)/len(group_A)
print("Average salary of Managers", int(avg))

