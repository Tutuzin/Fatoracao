import primo
def fatorate(number):
    #lista inicial de primos, incrementada com primo.py
    plist = [2,3,5,7]
    #divide o número por todos os primos
    for p in plist:
        pwr = 0
        #enquanto for divisivel:
        while number % p == 0:
            #divide-se e aumenta o expoente do número em 1
            pwr += 1
            number = number / p
        #se não for divisivel por esse numero primo
        else:
            if pwr != 0:
                print(p,'^',pwr)
        #pede o próximo primo se o número não está completamente dividido
        if p == plist[-1] and number != 1:
            primo.nextprime(plist)
loop = 'y'
while loop == 'y':
    number =int(input('Number to fatorate '))
    fatorate(number)
    loop = input('Fatorate again?(y/n)')
