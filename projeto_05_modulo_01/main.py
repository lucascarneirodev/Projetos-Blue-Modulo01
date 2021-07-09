from character import Character #biblioteca criada para as informações dos personagens.
from time import sleep #biblioteca criada para o jogo de interação.
from random import randint #biblioteca que gera aleatoriedade onde solicitado.
from datetime import datetime #biblioteca que atribui ao jogo a data em que ele está sendo jogado.
from clock import Time #biblioteca criada para o jogo de interação.
import os #Biblioteca do sistema operacional.

def lin():
    print('▬▬▬' * 32)       #A arte de relógio mostrada durante a execução do jogo.

if __name__ == '__main__':
    character = Character('',0,0,0,0,0)
    character.clean()
    clock = Time()
    character.stage = 1
    print(f'''                                        
                                ████      ██████████████      ████                          
                            ██░░░░████  ██░░░░░░░░░░██  ████░░░░██                        
                            ██░░░░░░░░░░██████████████████░░░░░░░░░░██                      
                        ██░░░░░░░░████        ██        ████░░░░░░░░██                    
                        ██░░░░████░░██    ██████████    ██░░████░░░░██                    
                            ████  ██░░██████░░░░░░░░░░██████░░██  ████                      
                                ████░░░░░░░░░░░░░░░░░░░░░░████                            
                                ██░░░░░░░░░░██████████░░░░░░░░░░██                          
                            ██░░░░░░██████          ██████░░░░░░██                        
                            ██░░░░░░██          ██          ██░░░░░░██                      
                            ██░░░░██    ██      ██      ██    ██░░░░██                      
                        ██░░░░░░██                          ██░░░░░░██                    
                        ██░░░░██  ██          ██          ██  ██░░░░██                    
                        ██░░░░██              ██████              ██░░░░██                  
                        ██░░░░██                ██                ██░░░░██                  
                        ██░░░░██                ██  ██            ██░░░░██                  
                        ██░░░░██  ████          ████████    ████  ██░░░░██                  
            ░░      ░░  ██░░░░██                    ██            ██░░░░██    ░░      ░░    
                        ██░░░░██      ██                  ██      ██░░░░██                  
                        ██░░██    ██                      ██    ██░░██                    
                        ██░░░░██        ██          ██        ██░░░░██                    
                            ██░░░░██    ██      ██      ██    ██░░░░██                      
                            ██░░░░░░██          ██          ██░░░░░░██                      
                            ██░░░░░░██████          ██████░░░░░░██                        
                                ██░░░░░░░░░░██████████░░░░░░░░░░██                          
                                ████░░░░░░░░░░░░░░░░░░░░░░████                            
                                    ██████░░░░░░░░░░██████                                
                                    ██████████████████████                                
    ░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░████████░░▓▓▓▓▓▓░░████████░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░

    {clock}
    O DESPERTADOR TOCOU E COMEÇA MAIS UM DIA DE TRABALHO NA JORNADA DO ESTAGIÁRIO.
    ''')
#Inicio da sequência de ações indicadas pelo usuário.
    ready = input('Você está preparado para jogar [S/N]? ').strip().upper()[0]
    while ready not in 'SN':
        ready = input('Opção inválida! Você está preparado para jogar [S/N]? ').strip().upper()[0]
    if ready == 'S':
        character.clean() # limpa o console.
        character.choice() # executa a função escolha para verificar o personagem.
        character.clean() # limpa o console.
        while True: # enquanto o jogador não quiser sair do jogo ou não matar o personagem.
            print(clock)
            print(character) # status inicial do personagem.
            lin()
            wakeup = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, olha a hora! 
            Temos muito o que fazer antes de ir ao trabalho. 
            O que você quer fazer?
            [1] Levantar
            [2] "Só mais 5 minutinhos e eu levanto"
            [0] SAIR DO JOGO
            ''')).strip().upper()[0] # opção do jogador.
# se o jogador inserir uma opção inválida, perguntará novamente até que a opção seja 0, 1 ou 2.
            while wakeup not in '012': 
                wakeup = str(input(f'''
            OPÇÃO INVÁLIDA!
            {character.name}, olha a hora! 
            Temos muito o que fazer antes de ir ao trabalho. 
            O que você quer fazer?
            [1] Levantar
            [2] "Só mais 5 minutinhos e eu levanto"
            [0] SAIR DO JOGO
            ''')).strip().upper()[0]
            while (wakeup=='2'):
                character.wakeup(wakeup)
                character.clean()
                clock.forward(10)
                character.statusDef()
                print(clock)
                print(character)
                lin()
                wakeup = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, olha a hora! 
            Temos muito o que fazer antes de ir ao trabalho. 
            O que você quer fazer?
            [1] Levantar
            [2] "Só mais 5 minutinhos e eu levanto"
            [0] SAIR DO JOGO ''')).strip().upper()[0]
# se o jogador inserir uma opção inválida, perguntará novamente até que a opção seja 0, 1 ou 2
                while wakeup not in '012': 
                    wakeup = str(input(f'''
            OPÇÃO INVÁLIDA!
            {character.name}, olha a hora! 
            Temos muito o que fazer antes de ir ao trabalho. 
            O que você quer fazer?
            [1] Levantar
            [2] "Só mais 5 minutinhos e eu levanto"
            [0] SAIR DO JOGO''')).strip().upper()[0]
# se o jogador escolher 1 ou 2, executa a função levantar() na classe Personagem.
# dentro da função fazer um while levantar == '2' para avançar o tempo no relógio enquanto o personagem não levanta
            if (wakeup == '1'): 
                character.wakeup(wakeup) 
                character.clean()
                clock.forward(5)
                character.statusDef()
                print(clock)
                print(character)
                lin()
                character.next_stage() # passa de fase no jogo
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            else: # se o jogador pressionar 0, ele desiste do jogo e o jogo encerra com a mensagem 
                print(character.giveup()) #contida na função desistir() na classe Personagem
                break
# se o jogador atingir uma das condições da função status() na classe Personagem, o jogo encerra porque o jogador perdeu.
            if character.statusPar() == True: 
                # character.statusPar()
                print(character.lost())
                break

            breakfast = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, olha o dia lindo que faz lá fora!
            Seu estômago deve estar roncando de fome, não? É hora de tomar um bom café da manhã
            O que você quer comer?
            [1] Frutas, pão, café e suco - um café da manhã bem reforçado!
            [2] A pizza amanhecida que você pediu ontem na janta com o resto de Coca-Cola
            [3] Café puro, sem açúcar e sem nada pra comer, pois você fica enjoado de manhã.
            [4] Não vai comer nem beber nada
            [0] SAIR DO JOGO

            ''')).strip().upper()[0]

            while breakfast not in '01234':
                breakfast = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, olha o dia lindo que faz lá fora!
            Seu estômago deve estar roncando de fome, não? É hora de tomar um bom café da manhã
            O que você quer comer?
            [1] Frutas, pão, café e suco - um café da manhã bem reforçado!
            [2] A pizza amanhecida que você pediu ontem na janta com o resto de Coca-Cola
            [3] Café puro, sem açúcar e sem nada pra comer, pois você fica enjoado de manhã.
            [4] Não vai comer nem beber nada
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]

            if (breakfast == '1'):
                character.meal(breakfast)
                character.clean()
                clock.forward(10)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (breakfast == "2"):
                character.meal(breakfast)
                character.clean()
                clock.forward(15)
                print(clock)
                print(character)
                lin()           
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (breakfast == "3"):
                character.meal(breakfast)
                character.clean()
                clock.forward(5)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (breakfast == "4"):
                character.meal(breakfast)
                character.clean()
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            else:
                print(character.giveup())
                break

            if character.statusPar() == True:
                # character.statusPar()
                print(character.lost())
                break


            shower = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, agora é hora de se preparar para o trabalho!
            Que tal tomar um banho para se refrescar e acordar de vez?
            [1] Sim, um banho é uma ótima ideia!
            [2] Nem a pau, um frio desses e eu vou tomar banho?
            [0] SAIR DO JOGO

            ''')).strip().upper()[0]

            while shower not in '012':
                shower = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, agora é hora de se preparar para o trabalho!
            Que tal tomar um banho para se refrescar e acordar de vez?
            [1] Sim, um banho é uma ótima ideia!
            [2] Nem a pau, um frio desses e eu vou tomar banho?
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]
            
            if (shower in '1'):
                character.takeshower(shower)
                character.clean()
                clock.forward(10)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (shower in '2'):
                character.takeshower(shower)
                character.clean()
                clock.forward(5)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            else:
                print(character.giveup())
                break
            
            if character.statusPar() == True:
                # character.statusPar()
                print(character.lost())
                break

            oneway = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, hora de ir trabalhar!
            Como você irá para o trabalho?
            [1] Vou a pé ou de bicicleta, para praticar um exercício físico 🚴
            [2] Vou de transporte público, para contribuir para menos emissão de carbono na atmosfera 🚌
            [3] Vou de Uber porque não sou obrigadx a passar perrengue 🚗
            [0] SAIR DO JOGO

            ''')).strip().upper()[0]

            while oneway not in '0123':
                oneway = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, hora de ir trabalhar!
            Como você irá para o trabalho?
            [1] Vou a pé ou de bicicleta, para praticar um exercício físico 🚴
            [2] Vou de transporte público, para contribuir para menos emissão de carbono na atmosfera 🚌
            [3] Vou de Uber porque não sou obrigadx a passar perrengue 🚗
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]
          
            if (oneway == '1'):
                character.route(oneway)
                character.clean()
                clock.forward(30)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (oneway == '2'):
                character.route(oneway)
                character.clean()
                clock.forward(25)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (oneway == '3'):
                character.route(oneway)
                character.clean()
                clock.forward(15)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            else:
                print(character.giveup())
                break
            
            if character.statusPar() == True:
                # character.statusPar()
                print(character.lost())
                break

            if clock.late() == True:
                print(character.lost())
                break
            
            else:
                situation1 = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, você chegou no trabalho e o programa que você alterou ontem
            não funciona! Vários clientes estão reclamando e ameaçando cancelar o serviço com
            a empresa. Seu chefe está maluco contigo e marca uma reunião para resolver o problema.
            
            O que você faz?
            [1] Respondo o chefe educadamente e falo que vou resolver o problema. Já sento na mesa e começo a trabalhar
            [2] Fico sem reação e não consigo falar nada para o chefe, vou ao banheiro e me tranco lá para refletir
            [3] Dou um tapa na mesa, me revolto e começo a gritar com o chefe. Vou para a minha mesa e não consigo produzir nada
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]
#Somente as opções 1, 2, 3 e 0 são dadas ao usuário, qualquer digito diferente desdes apresentará a msg:"OPÇÃO INVÁLIDA!"
                while situation1 not in '0123': 
                    situation1 = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, você chegou no trabalho e o programa que você alterou ontem
            não funciona! Vários clientes estão reclamando e ameaçando cancelar o serviço com
            a empresa. Seu chefe está maluco contigo e marca uma reunião para resolver o problema.
            
            O que você faz?
            [1] Respondo o chefe educadamente e falo que vou resolver o problema. Já sento na mesa e começo a trabalhar
            [2] Fico sem reação e não consigo falar nada para o chefe, vou ao banheiro e me tranco lá para refletir
            [3] Dou um tapa na mesa, me revolto e começo a gritar com o chefe. Vou para a minha mesa e não consigo produzir nada
            [0] SAIR DO JOGO

                    ''')).strip().upper()[0]

                if (situation1 == '1'):
                    character.bugwork(situation1)
                    character.clean()
                    clock.forward(15)
                    print(clock)
                    print(character)
                    lin()
                    character.next_stage()
                    print(f'Carregando a fase {character.stage:02d}')
                    sleep(2)
                elif (situation1 == '2'):
                    character.bugwork(situation1)
                    character.clean()
                    clock.forward(20)
                    print(clock)
                    print(character)
                    lin()
                    character.next_stage()
                    print(f'Carregando a fase {character.stage:02d}')
                    sleep(2)
                elif (situation1 == '3'):
                    character.bugwork(situation1)
                    character.clean()
                    clock.forward(25)
                    print(clock)
                    print(character)
                    lin()
                    character.next_stage()
                    print(f'Carregando a fase {character.stage:02d}')
                    sleep(2)
                else:
                    print(character.giveup())
                    break
                
            if character.statusPar() == True:
                # character.statusPar()
                print(character.lost())
                break

            clock.define(10,0)
            situation2 = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, após resolver o problema, seu chefe te chama na sala
            de reuniões para uma conversa. Você será alocado em um novo projeto, mais
            difícil e mais importante para a empresa.

            O que você faz?
            [1] Pergunta quanto ganhará de aumento para verificar se a realocação vale a pena
            [2] Agradece e aceita a oportunidade
            [3] Recusa a oportunidade e sai da sala de reuniões
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]

            while situation2 not in '0123':
                situation2 = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, após resolver o problema, seu chefe te chama na sala
            de reuniões para uma conversa. Você será alocado em um novo projeto, mais
            difícil e mais importante para a empresa.

            O que você faz?
            [1] Pergunta quanto ganhará de aumento para verificar se a realocação vale a pena
            [2] Agradece e aceita a oportunidade
            [3] Recusa a oportunidade e sai da sala de reuniões
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]

            if (situation2 == '1'):
                character.promotion(situation2)
                character.clean()
                clock.forward(20)
                print(clock)
                print(character)
                lin()
                character.next_stage()
            elif (situation2 == '2'):
                character.promotion(situation2)
                character.clean()
                clock.forward(20)
                print(clock)
                print(character)
                lin()
                character.next_stage()
            elif (situation2 == '3'):
                character.promotion(situation2)
                character.clean()
                clock.forward(20)
                print(clock)
                print(character)
                lin()
                character.next_stage()
            else:
                print(character.giveup())
                break

            clock.define(12,0)
            character.clean()
            print(clock)
            print(character)
            lin()
            print(f'Carregando a fase {character.stage:02d}')
            sleep(2)
            lunch = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, o primeiro tempo do trabalho já foi!
            Seu estômago deve estar roncando de fome, não? É hora do almoço.

            Onde você vai comer?
            [1] Restaurante chique com os chefes
            [2] Marmita com os outros estagiários
            [3] Pizza amanhecida que você trouxe de casa, sozinho na copa da empresa
            [4] Não vai comer nada
            [0] SAIR DO JOGO

            ''')).strip().upper()[0]

            while lunch not in '01234':
                lunch = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, olha o dia lindo que faz lá fora!
            Seu estômago deve estar roncando de fome, não? É hora de tomar um bom café da manhã
            O que você quer comer?
            [1] Restaurante chique com os chefes
            [2] Marmita com os outros estagiários
            [3] Pizza amanhecida que você trouxe de casa, sozinho na copa da empresa
            [4] Não vai comer nada
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]

            if (lunch == '1'):
                character.meal(lunch)
                character.clean()
                clock.forward(30)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (lunch == '2'):
                character.meal(lunch)
                character.clean()
                clock.forward(20)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (lunch == '3'):
                character.meal(lunch)
                character.clean()
                clock.forward(15)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (lunch == '4'):
                character.meal(lunch)
                character.clean()
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            else:
                print(character.giveup())
                break

            if character.statusPar() == True:
                # character.statusPar()
                print(character.lost())
                break

            clock.define(18,0)
            character.clean()
            print(clock)
            print(character)
            lin()
            print(f'Carregando a fase {character.stage:02d}')
            sleep(2)
            situation3 = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, após o expediente você é convidado para
            um happy hour com a galera da empresa.

            O que você vai fazer?
            [1] Topo e vou tomar uma cervejinha com o pessoal 🍻
            [2] Digo que estou cansado e não vou 😩
            [0] SAIR DO JOGO

            ''')).strip().upper()[0]

            while situation3 not in '012':
                situation3 = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, após o expediente você é convidado para
            um happy hour com a galera da empresa.

            O que você vai fazer?
            [1] Topo e vou tomar uma cervejinha com o pessoal 🍻
            [2] Digo que estou cansado e não vou 😩
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]
            
            if (situation3 == '1'):
                character.happyhour(situation3)
                character.clean()
                clock.forward(15)
                print(clock)
                print(character)
                lin()
                character.next_stage()
            elif (situation3 == '2'):
                character.happyhour(situation3)
                character.clean()
                clock.forward(5)
                print(clock)
                print(character)
                lin()
                character.next_stage()
            else:
                print(character.giveup())
                break
            
            if character.statusPar() == True:
                # character.statusPar()
                print(character.lost())
                break
            
            clock.define(20,0)
            character.clean()
            print(clock)
            print(character)
            lin()
            print(f'Carregando a fase {character.stage:02d}')
            sleep(2)
            back = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, hora de ir para casa!

            Como você irá embora?
            [1] Vou a pé ou de bicicleta, para praticar um exercício físico 🚴
            [2] Vou de transporte público, para contribuir para menos emissão de carbono na atmosfera 🚌
            [3] Vou de Uber porque não sou obrigadx a passar perrengue 🚗
            [0] SAIR DO JOGO

            ''')).strip().upper()[0]

            while back not in '0123':
                back = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, hora de ir para casa!

            Como você irá embora?
            [1] Vou a pé ou de bicicleta, para praticar um exercício físico 🚴
            [2] Vou de transporte público, para contribuir para menos emissão de carbono na atmosfera 🚌
            [3] Vou de Uber porque não sou obrigadx a passar perrengue 🚗
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]
            
            if (back == '1'):
                character.route(back)
                character.clean()
                clock.forward(30)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (back == '2'):
                character.route(back)
                character.clean()
                clock.forward(25)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (back == '3'):
                character.route(back)
                character.clean()
                clock.forward(15)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            else:
                print(character.giveup())
                break
            
            if character.statusPar() == True:
                # character.statusPar()
                print(character.lost())
                break

            dinner = str(input(f'''
            Fase {character.stage:02d}
            {character.name}, Até que enfim cheguei em casa!!
            Estou morrendo de fome 🍽

            Onde você vai comer?
            [1] Preparar uma janta deliciosa 🍲
            [2] Comer na rua
            [3] Usar seu Cupom de 10% no iFood e pedir comida 🏍️
            [4] Não vai comer nada e deitar na cama
            [0] SAIR DO JOGO

            ''')).strip().upper()[0]

            while dinner not in '01234':
                dinner = str(input(f'''
            OPÇÃO INVÁLIDA!
            Fase {character.stage:02d}
            {character.name}, Até que enfim cheguei em casa!!
            Estou morrendo de fome 🍽

            Onde você vai comer?
            [1] Preparar uma janta deliciosa 🍲
            [2] Comer na rua
            [3] Usar seu Cupom de 10% no iFood e pedir comida 🏍️
            [4] Não vai comer nada e deitar na cama
            [0] SAIR DO JOGO

                ''')).strip().upper()[0]

            if (dinner == '1'):
                character.meal(dinner)
                character.clean()
                clock.forward(30)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (dinner == '2'):
                character.meal(dinner)
                character.clean()
                clock.forward(20)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (dinner == '3'):
                character.meal(dinner)
                character.clean()
                clock.forward(40)
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            elif (dinner == '4'):
                character.meal(dinner)
                character.clean()
                print(clock)
                print(character)
                lin()
                character.next_stage()
                print(f'Carregando a fase {character.stage:02d}')
                sleep(2)
            else:
                print(character.giveup())
                break

            if character.statusPar() == True:
                # character.statusPar()
                print(character.lost())
                break
            else:
                print(character.win())

            if character.genidentity() == True:
                character.genidentity()
                break

            again = input('Deseja jogar novamente [S/N]? ').strip().upper()[0]
            while again not in 'SN':
                again = input('Opção inválida! Deseja jogar novamente [S/N]? ').strip().upper()[0]
                
            if again == 'S':
                clock.days += 1
                clock.define(6,0)
                character.newday(again)
            else:
                print('Obrigado por jogar!')
                break

    else:
        character.clean()
        print(character.giveup())