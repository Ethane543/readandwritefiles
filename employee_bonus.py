import csv

employee_data = open('employee_data.csv', 'r')

employee_file = csv.reader(employee_data)

next(employee_file)

for rec in employee_file:
    salary = float(rec[3])
    bonus = float(rec[7]) * salary
    pay = salary + bonus

    print('\n')
    print(f'Name: {rec[1]}')
    print(f'Salary: $ {salary:,.2f}')
    print(f'Bonus:  $  {bonus:,.2f}')
    print(f'Pay:    $ {pay:,.2f}')
   