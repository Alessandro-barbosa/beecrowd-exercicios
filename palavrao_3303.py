while True:
    try:
        palavra = input().lower()
        contador = 0
        for i in range(len(palavra)):
            contador += 1
        print("palavrao" if contador >= 10 else "palavrinha")
    except EOFError:
        break