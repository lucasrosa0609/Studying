# Rewrite your pay computation to give the employee 1.5 times the horly rate
# for hours worked above 40 hours

enter_hours = input('Enter Hours: ')
enter_rate = input('Enteder Rate: ')

pay = float(enter_hours) * float(enter_rate)

if float(enter_hours) > 40:
    print('Overtime, all hours above 40 are being multiplied by 1.5')
    pay = 40 * float(enter_rate)
    excessive_hours = float(enter_hours) - 40
    excessive_hours_payment = (excessive_hours * float(enter_rate)) * 1.5
    print(pay + excessive_hours_payment)
else:
    print('Regular hour')
    print(pay)


