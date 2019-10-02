import re 

text = open('Employees.txt', 'r')
txt = text.read()

employee = re.findall(r'[A-Z]\w+', txt)
ages = re.findall(r'\b\d{2}\b', txt)
salarys = re.findall(r'\d{5}', txt)
lnames = employee[::2]
names = employee[1::2]

employees = [[lname,name,age,salarys] for lname,name,age,salarys in zip(lnames,names,ages,salarys)]

convert_employees = []

for i in range(len(employees)):
	local_dict = {}

	local_dict['lname'] = employees[i][0]
	local_dict['name'] = employees[i][1]
	local_dict['age'] = employees[i][2]
	local_dict['salary'] = employees[i][3]

	convert_employees.append(local_dict)

print(convert_employees)
