import sys

print('AQUI VAI UM TÍTULO MANEIRO EM ARTE COM CARACTERES ESCRITO "DETETIVE"')

suspeita = 0

pergunta01      =   input("\nVocê telefonou para a vítima?[S/N]").upper()
if pergunta01[0]==  'S':
  suspeita      +=  1
  print(pergunta01[0])
elif  pergunta01[0]==  'N':
  suspeita      = suspeita
else:
  print('''\n                           Você não sabe falar direito? Ou não quer cooperar? 
  Isso não deixam as coisas favoráveis no seu interrogatório, isso com certeza será levado em consideração na conclusão do caso.
                      E além disso iremos te prender preventivamente até decidir cooperar com as autoridades!''')
  sys.exit('\nSeu interrogatório foi interrompido, mas você vai passar a noite na cadeia.')

pergunta02      =   input("\nVocê esteve no local do crime?[S/N]").upper()
if  pergunta02[0]  =='S':
  suspeita    +=  1
elif  pergunta02[0]==  'N':
  suspeita = suspeita
else:
  suspeita      +=  1
  print('''\n                           Você não sabe falar direito? Ou não quer cooperar? 
  Isso não deixam as coisas favoráveis no seu interrogatório, isso com certeza será levado em consideração na conclusão do caso.
                      E além disso iremos te prender preventivamente até decidir cooperar com as autoridades!''')
  sys.exit('\nSeu interrogatório foi interrompido, mas você vai passar a noite na cadeia.')

pergunta03      =   input("\nVocê mora perto da vítima?[S/N]").upper()
if  pergunta03[0]  ==  'S':
  suspeita    +=  1
elif pergunta03[0] ==  'N':
  suspeita      = suspeita
else:
  suspeita      +=  1
  print('''\n                           Você não sabe falar direito? Ou não quer cooperar? 
  Isso não deixam as coisas favoráveis no seu interrogatório, isso com certeza será levado em consideração na conclusão do caso.
                      E além disso iremos te prender preventivamente até decidir cooperar com as autoridades!''')
  sys.exit('\nSeu interrogatório foi interrompido, mas você vai passar a noite na cadeia.')

pergunta04      =   input("\nVocê devia para a vítima?[S/N]").upper()
if  pergunta04[0]  ==  'S':
  suspeita    +=  1
elif pergunta04[0] ==  'N':
  suspeita      = suspeita
else:
  suspeita      +=  1
  print('''\n                           Você não sabe falar direito? Ou não quer cooperar? 
  Isso não deixam as coisas favoráveis no seu interrogatório, isso com certeza será levado em consideração na conclusão do caso.
                      E além disso iremos te prender preventivamente até decidir cooperar com as autoridades!''')
  sys.exit('\nSeu interrogatório foi interrompido, mas você vai passar a noite na cadeia.')

pergunta05      =   input("\nVocê já trabalhou com a vítima?[S/N]").upper()
if  pergunta05[0]  ==  'S':
    suspeita    +=  1
elif  pergunta03[0]==  'N':
  suspeita      = suspeita
else:
  suspeita      +=  1
  print('''\n                           Você não sabe falar direito? Ou não quer cooperar? 
  Isso não deixam as coisas favoráveis no seu interrogatório, isso com certeza será levado em consideração na conclusão do caso.
                      E além disso iremos te prender preventivamente até decidir cooperar com as autoridades!''')
  sys.exit('\nSeu interrogatório foi interrompido, mas você vai passar a noite na cadeia.')

if suspeita == 2:
    print('\nEssa pessoa é suspeita.')
elif 3 <= suspeita <= 4:
    print('\nEssa pessoa só pode ser um cúmplice.')
elif suspeita >= 5:
    print('\nPrendam o meliante, ele com certeza é o assassino.')
else:
    print('\nPor enquanto não temos suspeitos, esse cara é inocente.')

suspeita = 0