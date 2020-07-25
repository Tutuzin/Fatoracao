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
while True:
    while True:
        try:
            number =int(input('Number to fatorate: '))
            break
        except ValueError:
            print('Try again')
    fatorate(number)
    try:
        loop = input('Fatorate again?(y/n)')
        if loop in ('y','yes','s','sim'): continue
        elif loop in ('n','no','nao','não',''): break
        else: raise NameError('Input Inesperado')
    except NameError:
        print('Tente Novamente')
