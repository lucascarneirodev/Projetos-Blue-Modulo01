@import time
@import ascii

print('Jogo detetive')

suspeita    = 0

pergunta01  =   input("Você telefonou para a vítima?[S/N]").upper()
if  pergunta01=='S':
    suspeita+=1
pergunta02  =   input("Você esteve no local do crime?[S/N]").upper()
if  pergunta02=='S':
    suspeita+=1
pergunta03  =   input("Você mora perto da vítima?[S/N]").upper()
if  pergunta03=='S':
    suspeita+=1
pergunta04  =   input("Você devia para a vítima?[S/N]").upper()
if  pergunta04=='S':
    suspeita+=1
pergunta05  =   input("Você já trabalhou com a vítima?[S/N]").upper()