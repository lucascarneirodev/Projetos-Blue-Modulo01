#Class Charater é uma bliblioteca criada para dar atribuições aos personagens deste jogo de interação. 
#Nela conSta as características, habilidades, preferências e comportamentos típicos de cada geração aqui indicada, 
# a geração Boomer e a Geração Z.

import os               #Biblioteca do sistema operacional.
from clock import Time  #biblioteca criada para o jogo de interação.
from time import sleep  #biblioteca para efeitos de pausa no decorrer das interações do jogo.
from random import randint #biblioteca que gera aleatoriedade onde solicitado.
from datetime import datetime #biblioteca que atribui ao jogo a data em que ele está sendo jogado.

class Character:        #inicialização da classe de Personagens.
    def __init__(self, name, age, generation, energy=0, money=0, anxiety=0,status=0):
        self.__name = name
        self.__age = age
        self.__energy = energy
        self.__money = money
        self.__anxiety = anxiety
        self.__status = status
        self.__generation = generation

    def __str__(self):      #definição para mostragem do personagem escolhido por rodada, com seus respectivos status.
        return f'''
        ESTAGIÁRIO {self.generation.upper()}:

        Personagem: {self.name}
        Idade: {self.age}
        Energia: {self.energy}
        Dinheiro: {self.money}
        Ansiedade: {self.anxiety}
        Geração: {self.generation}
        Status Atual: {self.statusDef()}

        '''

    def statusDef(self):        #De acordo com as escolhas feitas, o status varia, podendo ter como consequência 
        if self.__status > 0:   #a mudança de geração dos personagens.
            return 'Boomer'
        else:
            return 'Geração Z'

    @property
    def name(self):
        return self.__name 

    @property
    def age(self):
        return self.__age

    @property
    def energy(self):
        return self.__energy

    @property
    def generation(self):
        return self.__generation
    
    @property
    def status(self):
        return self.__status

    @energy.setter
    def energy(self, value):
        self.__energy += value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money += value

    @property
    def anxiety(self):
        return self.__anxiety

    @anxiety.setter
    def anxiety(self, value):
        self.__anxiety -= value

    
    def newday(self, choice):   #De acordo com a escolha do usuário, os índices do status pode aumentar ou diminuir.
        if choice == 'S':       #Essas variações podem melhorar ou piorar a saúde do personagem, e pode até matá-lo.
            self.__energy += 50
            self.__anxiety -= 20

    def wakeup(self, choice):   #De acordo com a escolha do usuário, os índices do status pode aumentar ou diminuir.
        if choice == '1':       #Essas variações podem melhorar ou piorar a saúde do personagem, e pode até matá-lo.
            self.__energy -= 5
            self.__money -= 0
            self.__anxiety += 10
            self.__status += 5
        else:
            self.__energy += 5
            self.__money -= 0
            self.__anxiety -= 10
            self.__status -= 5

    def meal(self, choice):     #os tipos de refeições escolhidas podem afetar a saúde e o financeiro do personagem.
        if choice == '1':
            self.__energy += 5      #O uso de if, elif e else é um agente condicional nessa parte do código,
            self.__money -= 20      #Esse uso faz com que a escolha seja a única a ser mostrada na execução.
            self.__anxiety -= 20
            self.__status -= 10
            
        elif choice == '2':
            self.__energy += 5
            self.__money -= 5
            self.__anxiety -= 5
            self.__status += 5

        elif choice == '3':
            self.__energy -= 10
            self.__money += 0
            self.__anxiety += 5
            self.__status -= 0

        else:
            self.__energy -= 20
            self.__money += 0
            self.__anxiety += 20
            self.__status += 0

    def takeshower(self, choice):   #essa escolha afeta o tempo e infere a saúde do personagem.
        if choice == '1':
            self.__energy -= 5
            self.__money -= 0
            self.__anxiety -= 10
            self.__status += 5
            
        else:
            self.__energy -= 0
            self.__money += 0
            self.__anxiety += 10
            self.__status -=5 

    def route(self, choice):           
        if choice == '1':
            self.__energy -= 10 
            self.__money += 0
            self.__anxiety -= 10
            self.__status += 5
            
        elif choice == '2':
            self.__energy -= 5
            self.__money -= 5
            self.__anxiety += 5
            self.__status += 0

        else:
            self.__energy -= 5
            self.__money -= 20
            self.__anxiety += 0
            self.__status -= 5

    def bugwork(self, choice):  #essa escolha afeta os níveis de ansiedade do personagem, o que pode ser nocivo à vida dele.
        if self.anxiety > 35:
            print('Sua ansiedade está alta demais, você não consegue manter a paciência.')
            sleep(5)
            choice == '3'
            self.__energy -= 20
            self.__money -= 0
            self.__anxiety += 20
            if self.generation=='boomer':
                self.__status-=10
            else:
                self.__status+=10
        
        if choice == '1':
            self.__energy -= 10 
            self.__money += 0
            self.__anxiety -= 10
            self.__status += 10
            
        elif choice == '2':
            self.__energy -= 10
            self.__money -= 0
            self.__anxiety += 10
            self.__status -= 10
        
        else:
            self.__energy -= 20
            self.__money -= 0
            self.__anxiety += 20
            if self.generation=='boomer':
                self.__status-=10
            else:
                self.__status+=10

    def promotion(self,choice):
        if self.anxiety > 35:
            print('Sua ansiedade está alta demais, você não consegue manter a paciência. Seu chefe te rebaixa de cargo!')
            sleep(3)
            choice == '3'
            self.__energy -= 20
            self.__money -= 0
            if self.generation=='boomer':
                self.__status-=10
            else:
                self.__status+=10
        else:
            if choice == '1':
                print('''O chefe diz que precisa analisar a possibilidade de aumento, mas
                retira a proposta ao notar que você não se empolgou com a oportunidade...
                Você receberá 50 dinheiros pelo dia de trabalho''')
                sleep(3)
                self.__energy -= 10 
                self.__money += 50
                self.__anxiety -= 10
                self.__status += 10
                
            elif choice == '2':
                print('''Você recebe a notícia de que ganhará um aumento. Parabéns!
                Você receberá 70 dinheiros pelo dia de trabalho''')
                sleep(3)
                self.__energy -= 10
                self.__money += 70
                self.__anxiety += 10
                self.__status -= 10
            
            else:
                print('''Seu chefe te rebaixa de cargo!
                Você receberá 30 dinheiros pelo dia de trabalho''')
                sleep(3)
                self.__energy -= 20
                self.__money += 30
                self.__anxiety += 20
                if self.generation=='boomer':
                    self.__status-=10
                else:
                    self.__status+=10
    
    def happyhour(self, choice):
        if choice == '1':
            self.__energy -= 20
            self.__money -= 0
            self.__anxiety -= 20
            self.__status -= 10
            
        else:
            self.__energy -= 5
            self.__money += 0
            self.__anxiety += 20
            self.__status +=10
#Esse é o programa principal, nele consta as informações de cada personagem.
#Escolhemos a mostragem geral dos dois personagens afim de que, o usuário 
#fique ciente das diferenças entre as duas gerações.

    def choice(self):
        for i in range(5,0,-1):
            print(f'CARREGANDO INFORMAÇÕES EM {i}...\n')
            sleep(1)
            os.system('cls||clear')

        print('''BOOMER:

        Dona Cida está sempre olhando para a janela ou apoiada em sua sacada
        observando o que acontece na vizinhança. Não perde uma fofoca no seu bairro
        e ao mesmo tempo cuida da sua vida e da sua casa como ninguém.

        Nascimento: 1957
        Estilo de música preferida: Bossa nova
        Comida predileta: Mandioca
        Novela preferida: Tieta do Agreste
        Mora em casa própria desde os 19 anos quando casas ainda eram trocadas por linhas telefônicas.
        Profissão: Aposentada
        Hobbie: Ficar na janela cuidando da vida dos outros.

        Inteligência: 4
        Força: 1
        Carisma: 5
        Foco: 3

        Habilidade especial:
        Fuxiqueira.


        GERAÇÃO Z:

        Enzo Gabriel sempre está olhando para alguma tela, 
        tem dificuldades de se concentrar em uma coisa mas estranhamente 
        tem facilidade em ser multitarefa, nunca anda sem colírio nos bolsos.

        Nascimento: 2003
        Estilo de música preferida: Kpop
        Sobremesa preferida: Brizadeiro e Bolinho Espacial
        Série preferida: qualquer série que tenham vampiros ou zumbis (as vezes zumbis e vampiros se casando)
        Mora com os pais
        Profissão: Jovem Aprendiz
        Hobbie: Streamer

        Inteligência: 5
        Força: 3
        Carisma: 1
        Foco: 0

        Habilidade especial:
        Ser multitarefa - consegue aprender qualquer coisa rapidamente mas não domina nenhum tema.
        ''')

        choice = str(input('''
        CHOOSE YOUR FIGHTER
        [1] DONA CIDA
        [2] ENZO GABRIEL
        [3] ALEATÓRIO

        ''')).strip().upper()[0]
        while choice not in '123':
            choice = str(input('''
            OPÇÃO INVÁLIDA!
            CHOOSE YOUR FIGHTER
            [1] DONA CIDA
            [2] ENZO GABRIEL
            [3] ALEATÓRIO
            ''')).strip().upper()[0]
        if choice == '3':
            choice = str(randint(1,2))
        if choice == '1':
            self.__name = 'Dona Cida'
            self.__age = datetime.now().year - 1957
            self.__energy = 50
            self.__money = 100
            self.__anxiety = 0
            self.__generation = 'Boomer'
            self.__status = 1
        else:
            self.__name = 'Enzo Gabriel'
            self.__age = datetime.now().year - 2003
            self.__energy = 100
            self.__money = 50
            self.__anxiety = 50
            self.__generation = 'Geração Z'
            self.__status = -1

        character = Character(self.__name, self.__age, self.__energy, self.__money, self.__anxiety, self.__status)
        print(f'''
        PERSONAGEM ESCOLHIDO!!
        {character.name.upper()}
        CARREGANDO A PRÓXIMA FASE...
        ''')
        sleep(5)

    def next_stage(self):
        self.stage += 1

    def clean(self):
        os.system('cls||clear')
#A partir daqui, é mostrada a finalização do jogo e as consequências das escolhar do seu decorrer.
    def statusPar(self):
        if self.energy <= 0 or self.money <= 0 or self.anxiety >= 150:
            if self.energy <= 0:
                print(f'{self.name} morreu por falta de energia.')
            elif self.money <= 0:
                print(f'{self.name} ficou sem dinheiro.')
            elif self.anxiety >= 150:
                print(f'{self.name} morreu de ansiedade.')
            return True

    def win(self):
        return '''VOCÊ VENCEU! PARABÉNS, CHEGOU VIVO AO FINAL DE UM DIA DE TRABALHO!'''

    def lost(self):
        return '''VOCÊ PERDEU! FIM DE JOGO...'''

    def genidentity(self):
        if self.statusDef() != self.__generation:
            print(f'Você é {self.__generation} e se comportou como um {self.statusDef()} durante o dia! FIM DE JOGO...')
            return True

    def giveup(self):
        return '''
        JÁ DESISTIU?
        TINHA QUE SER O ESTAGIÁRIO MESMO!
        FIM DE JOGO...
        '''