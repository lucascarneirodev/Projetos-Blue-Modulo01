import random

#Declaração de variáveis
scoreBoard={}
scoreResult = {}
roundResult = {}
scoreList   = []
podium      = {}
podiumList  = []
tempPodium  = []

#Loop do jogo inteiro
while True:
    #inicialização e limpeza de variáveis, listas e dicionários
    draws=1
    totalDraws=0
    rounds=int(input('Digite número de rodadas: '))
    players=int(input('Número de jogadores: '))
    scoreBoard.clear()
    roundResult.clear()
    scoreList.clear()
    scoreResult.clear()
    podiumList.clear()
    podium.clear()
    tempPodium.clear()

    #definir quantidade de dados a serem rolados baseado no número de jogadores
    #para diminuir frequencia de empates e evitar erro na função sample()
    if players > 5 or rounds>11: dices = round(players/5)
    else: dices = 2

    #laço de rolagem de dados
    for p in range(1,rounds+1):
        #  variável 'n' será usada para ajudar a definir o index do dicionario aonde o resultado dos
        # rounds são armazenados
        if p < 10: n = f'0{str(p)}'
        else: n = str(p)
        scoreBoard['round{}'.format(n)]=random.sample(range(1,6*dices),k=players)
        # print('round{}'.format(n))
        # print(scoreBoard['round{}'.format(n)])
        if (1+scoreBoard["round{}".format(n)].index(max(scoreBoard["round{}".format(n)])))<10:
            m= f'0{1+scoreBoard["round{}".format(n)].index(max(scoreBoard["round{}".format(n)]))}'
        else:
            m=1+scoreBoard["round{}".format(n)].index(max(scoreBoard["round{}".format(n)]))
        roundResult[f'round{n}: ']= f'player{m}'
        scoreList.append(roundResult[f'round{n}: '])

    #Copiando de uma lista a pontuação de cada jogador  para adicionar a um dicionário
    for p in range(1,players+1):
        if p < 10: n = f'0{str(p)}'
        else: n = str(p)
        scoreResult[f'player{n}']=scoreList.count(f'player{n}')
        podiumList.append(scoreResult[f'player{n}'])

    #Loop de desempate
    while draws>0:
        draws=0
        for p in range(1,players+1): 
            if p < 10: n = f'0{str(p)}'
            else: n = str(p)
            for z in range(1,players+1):
                m = ''
                if z < 10: m = f'0{str(z)}'
                else: m = str(z)
                #Condicional para impedir desempate entre o mesmo player
                if n!=m:
                    #Condicional que verifica se um resultado de um jogador é igual a outro, 
                    # caso seja ocorre uma partida de desempate entre os dois jogadores
                    if scoreResult[f'player{n}']==scoreResult[f'player{m}']:
                        p1=random.sample(range(1,6),1)
                        p2=random.sample(range(1,6),1)
                        totalDraws+=1
                        if p1>p2:
                            scoreResult[f'player{n}']+=1
                            podiumList[p-1]+=1
                            draws+=1
                        else:
                            scoreResult[f'player{m}']+=1
                            podiumList[z-1]+=1
                            draws+=1

    print(f'\nTotal de desempates realizados nessa partida: {totalDraws}')
    print(f'\nQuantidade de dados utilizados em cada round: {dices}')


    #copiando lista de pontuações para uma lista que será alterada enquanto verifica
    # a posição de cada jogador
    tempPodium  = podiumList.copy()

    #laço que contabiliza os pontos e define a posição de cada colocado
    print(f'\n{30*"="}RESULTADO{30*"="}')
    for p in range(0,players):
        maxPodium   =max(tempPodium)#vencedor da rodada
        maxIndex    =tempPodium.index(maxPodium)#indice do vencedor
        n = ''#string usada para nomear os vencedores
        if maxIndex+1 < 10: n = f'0{str(maxIndex+1)}'
        else: n = str(maxIndex+1)
        m = ''#string usada para nomear os vencedores
        if p+1 < 10: m = f'0{str(p+1)}'
        else: m = str(p+1)
        podium[f'{m}º Colocado: ']=f'Player{n}  Vitórias: {podiumList[maxIndex]}'
        print(f"{m}º Colocado: {podium[f'{m}º Colocado: ']}")
        tempPodium[maxIndex]=-1


    if input('Jogar novamente? [S/N]: ').upper()=='N' : 
        break