# Rewrite your program using try and except so that your program handles
# non-numeric input gracefuly by printing a message and exiting the program


enter_hours = input('Enter Hours: ')
enter_rate = input('Enter Rate: ')
try:
    float(enter_hours), float(enter_rate)
except:
    enter_hours = -1
    enter_rate = -1

if float(enter_hours) > 0:
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
else:
    print('Not a number')

print('All done')