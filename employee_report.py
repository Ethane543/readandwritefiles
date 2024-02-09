import csv

employee_data = open('employee_data.csv', 'r')

employee_data_file = csv.reader(employee_data)

next(employee_data_file)

high_efficient = []
low_efficient = []

employees_40s = []
employees_30s = []
employees_20s = []

countage_20 = 0
countage_30 = 0
countage_40 = 0

for rec in employee_data_file:
    name = rec[1]
    age = float(rec[2])
    efficiency = float(rec[5])/float(rec[4])
    
    if efficiency >= 2:
        high_efficient.append(name)

    elif efficiency <= 1:
        low_efficient.append(name)

    if 20 <= age < 30:
        countage_20 += 1
        employees_20s.append(name)

    elif 30 <= age < 40:
        countage_30 += 1
        employees_30s.append(name)

    elif age >= 40:
        countage_40 += 1
        employees_40s.append(name)

print('High Efficiency Individuals:')

for name in high_efficient:
    print(name)

print('\n')

print('Low Efficiency Individuals:')

for name in low_efficient:
    print(name)

print('\n')

print('Employees in their 40s:')

for name in employees_40s:
    print(name)

print('\n')
print(f"Total Number of Employees in their 40s: {countage_40}")
print('\n')

print('Employees in their 30s:')

for name in employees_30s:
    print(name)

print('\n')
print(f"Total Number of Employees in their 30s: {countage_30}")
print('\n')

print('Employees in their 20s:')

for name in employees_20s:
    print(name)

print('\n')
print(f"Total Number of Employees in their 20s: {countage_20}")