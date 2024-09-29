password = 'polivatarbys'



while True:
    userinput = input('Пароль: ')
    if userinput == password:
        print("ВЕрный пароль")
    elif userinput == 'exit':
        exit()
    else:
        print('Пароль невеный>:(')