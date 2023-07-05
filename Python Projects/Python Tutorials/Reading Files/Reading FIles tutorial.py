#Open file
employee_file = open("employee.txt", "r")
for employee in employee_file.readlines():
    #Put file into an array
    print(employee)

#Read file line by line
#print(employee_file.readline()

#Always close file
employee_file.close()