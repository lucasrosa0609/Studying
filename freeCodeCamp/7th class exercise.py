# rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters

def computepay(hours, rate):
    hours = float(hours)
    rate = float(rate)
    payment = hours * rate
    if hours > 40:
        print('Overtime, all hours above 40 are being multiplied by 1.5')
        payment = 40 * rate
        excessive_hours = hours - 40
        excessive_hours_payment = (excessive_hours * rate) * 1.5
        print(payment + excessive_hours_payment)
    else:
        print('Regular hour')
        print(payment)


enter_hours = input('Enter Hours: ')
enter_rate = input('Enter Rate: ')

try:
    float(enter_hours), float(enter_rate)
except:
    enter_hours = -1
    enter_rate = -1

if float(enter_hours) > 0:
    computepay(enter_hours, enter_rate)
else:
    print('Not a number')

print('All done')
