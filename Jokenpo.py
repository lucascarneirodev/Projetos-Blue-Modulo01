import random
import time

print('\nJokenpô\n\n')

pontosComputador= 0
pontosJogador   = 0
jokenpo = ['Pedra','Papel','Tesoura']
while True: 
    time.sleep(1)
    for r in range(0,int(input('Digite quantas jogadas quer realizar: '))):
        time.sleep(2)
        print(f'''
            Escolha sua jogada
            [0] - Pedra
            [1] - Papel
            [2] - Tesoura
            ''')
        time.sleep(2)
        jogada = int(input('\nDigite um número entre as opções para sua jogada: '))
        jogadaComputador = random.randint(0,2)

        print('Jo...')
        time.sleep(1)  
        print('Ken...')
        time.sleep(1)
        print('Pô!!!')
        time.sleep(2)
        print(f'''
            Você:   {jokenpo[jogada]}    X       Computador:    {jokenpo[jogadaComputador]}
        ''')
        time.sleep(2)
        if jogada==jogadaComputador:
            time.sleep(1)
            print('Empate!')
        else:
            if jogada == 0:
                if jogadaComputador == 1:
                    time.sleep(1)
                    print('O computador venceu essa rodada!')
                    pontosComputador+=1
                else:
                    time.sleep(1)
                    print('Você venceu a jogada!!!')
                    pontosJogador+=1
            if jogada == 1:
                if jogadaComputador == 2:
                    time.sleep(1)
                    print('O computador venceu essa rodada!')
                    pontosComputador+=1
                else:
                    time.sleep(1)
                    print('Você venceu a jogada!!!')
                    pontosJogador+=1
            if jogada == 2:
                if jogadaComputador == 0:
                    time.sleep(1)
                    print(f'''
                        Você:   {jokenpo[jogada]}    X       Computador:    {jokenpo[jogadaComputador]}
                    ''')
                    print('O computador venceu essa rodada!')
                    pontosComputador+=1
                else:
                    time.sleep(1)
                    print('Você venceu a jogada!!!')
                    pontosJogador+=1
    time.sleep(1)
    print(f'''
                    Você:   {pontosJogador}    X       Computador    {pontosComputador}
                ''')
    if pontosJogador==pontosComputador:
        time.sleep(1)
        print('Foi um empate!')
    if pontosJogador>pontosComputador:
        time.sleep(1)
        print('Parabéns, você ganhou todas as partidas!!!')
    if  pontosJogador<pontosComputador:
        time.sleep(1)
        print('Você foi derrotado, previsível...')
        time.sleep(2)
        print('         ...Humano.')
    pontosComputador= 0
    pontosJogador   = 0
    time.sleep(2)
    repetir = input('\nGostaria de jogar novamente?[S/N] ').upper()
    if repetir[0]=='N':
        print('\nObrigado por jogar!')
        break
