print('Jogo detetive')

suspeita    =   0

pergunta01  =   input("Você telefonou para a vítima?[S/N]").upper().captalize()
if  pergunta01  =='S':
    suspeita+=1
pergunta02  =   input("Você esteve no local do crime?[S/N]").upper().captalize()
if  pergunta02  =='S':
    suspeita+=1
pergunta03  =   input("Você mora perto da vítima?[S/N]").upper().captalize()
if  pergunta03  =='S':
    suspeita+=1
pergunta04  =   input("Você devia para a vítima?[S/N]").upper().captalize()
if  pergunta04  =='S':
    suspeita+=1
pergunta05  =   input("Você já trabalhou com a vítima?[S/N]").upper().captalize()
if  pergunta05  =='S':
    suspeita+=1

if suspeita == 2:
    print('Essa pessoa é suspeita.')
elif suspeita == 3 or suspeita == 4:
    print('Essa pessoa só pode ser um cúmplice.')
elif suspeita == 5:
    print('Prendam o meliante, ele com certeza é o assassino.')
else:
    print('Por enquanto não temos suspeitos, esse cara é inocente.')