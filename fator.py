import primo
def fatorate(number):
    plist = [2,3,5,7]
    for p in plist:
        pwr = 0
        while number % p == 0:
            pwr += 1
            number = number / p
        else:
            if pwr != 0:
                print(p,'^',pwr)
        if p == plist[-1] and number != 1:
            primo.nextprime(plist)
loop = 'y'
while loop == 'y':
    number =int(input('Number to fatorate '))
    fatorate(number)
    loop = input('Fatorate again?(y/n)')
