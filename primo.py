def nextprime(plist):
    n = plist[-1]
    prime = True
    while prime:
        n += 1
        for p in plist:
            if n % p == 0:
                break
            else:
                if p == plist[-1]: plist.append(n); prime = False
    #print(plist)

