while True:
    try:
        p = int(input())
        j1, j2 = [int(x) for x in input().split()]
        m1, m2 = [int(x) for x in input().split()]
        cartas_jogadas = [int(x) for x in input().split()]
        contador_cartas = 0
        perdeuMaria = False
        perdeuJoao = False
        if j1 > 10:
            j1 = 10
        if j2 > 10:
            j2 = 10
        if m1 > 10:
            m1 = 10
        if m2 > 10:
            m2 = 10

        p_joao = j1 + j2
        p_maria = m1 + m2

        for i in cartas_jogadas:  # somando a pontuacao dentro das cartas que foram jogadas
            p_joao += i
            p_maria += i
        cartas_jogadas.append(j1)  # Adicionando as cartas que já foram sorteadas
        cartas_jogadas.append(j2)
        cartas_jogadas.append(m1)
        cartas_jogadas.append(m2)

        carta_maria = abs(p_maria - 23)  # carta para maria ganhar
        carta_joao = abs(p_joao - 24)  # carta para joao perder

        if carta_maria <= carta_joao:
            for i in cartas_jogadas:  # percorrendo a carta que falta pra ganhar dentro da lista
                if i >= 10:
                    i = 10
                if carta_maria == i:
                    contador_cartas += 1
                if contador_cartas >= 4:
                    i = 0
                    carta_maria += 1
                    contador_cartas = 0
                if (carta_maria + p_maria) > 23:
                    perdeuMaria = True
                    break

        else:
            for j in cartas_jogadas:  # percorrendo a carta que falta pra joao perder dentro da lista
                if j >= 10:
                    j = 10
                if carta_joao == j:
                    contador_cartas += 1
                if contador_cartas >= 4:
                    j = 0
                    carta_joao += 1
                    contador_cartas = 0
                if (carta_joao + p_joao) > 24:
                    perdeuJoao = True
                    break
                perdeuJoao = True

        if perdeuJoao == True:
            print(carta_joao)
        elif perdeuMaria == False:
            print(carta_maria)
        else:
            print("-1")
    except EOFError:
        break
