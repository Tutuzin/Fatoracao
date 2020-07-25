def nextprime(plist):
    #seleciona o maior numero primo da lista
    n = plist[-1]
    #ativa o loop
    prime = True
    while prime == False:
        #próximo número natural para checar
        n += 1
        #testa se é primo
        for p in plist:
            if n % p == 0:
                break
            else:
                #se for primo, adiciona a lista de primos
                if p == plist[-1]: plist.append(n); prime = False
    #print(plist)

