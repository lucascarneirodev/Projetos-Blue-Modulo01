#Class Time é uma biblioteca criada para dar definição de tempo atribuida às escolhas feitas pelo usuário.
#Podendo gerar ganho ou perda de tempo em suas interações durante o processo, e o decorrer do processo.
class Time:
    def __init__(self): #Inicialização da Classe.
        self.hours = 6
        self.minutes = 0
        self.days = 1
    
    def __str__(self): 
        return f"Dia {self.days}, {self.hours:02d}:{self.minutes:02d}"
    
    def forward(self, minutes):     #definição da função para passagem de tempo.
        self.minutes += minutes
        while(self.minutes >= 60):
            self.minutes -= 60
            self.hours += 1
        while(self.hours >= 24):
            self.hours -= 24
            self.days += 1
    
    def late(self):             #definição da função em caso de escolhas que geram atrasos.
        if self.hours >= 8 and self.minutes > 0 or self.hours > 8:
            return True
    
    def define(self, hours, minutes):   #definição do tempo decorrido no jogo, seja em dias, horas ou minutos.
        self.hours = hours
        self.minutes = minutes
        return f"Dia {self.days}, {self.hours:02d}:{self.minutes:02d}"