while True:
    reply = input("Wpisz tekst: ")
    if reply == 'stop': break
    print(reply.upper())


while True:
    reply = input("Wpisz tekst: ")
    if reply == 'stop': break
    elif not reply.isdigit(): print('blad!')
    else: print(int(reply ** 2))


while True:
    reply = input("Wpisz tekst: ")
    if reply == 'stop': break
    try:
        reply = int(reply)
    except:
        print('blad!')
    else:
        print(int(reply ** 2))

while True:
    reply = input("Wpisz tekst: ")
    if reply == 'stop': break
    elif not reply.isdigit(): print('blad!')
    else:
        num = int(reply)
        if num < 20:
            print('malo')
        else:
            print(num ** 2)
