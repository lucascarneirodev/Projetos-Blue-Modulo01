from datetime import date



#list of candidates
candidates  = ['Carlos','Maria','José','Voto Nulo','Voto em Branco']
votes       = {}


#Age validation function
def autoriza_voto():
    while True:#loop to test birth year input
        year = input('Digite o seu ano de nascimento[yyyy]: ')#birth year variable
        error=0#variable to count errors
        try: #test 'year'
            int(year)
        except: #input was incorrectly filled in 
            print('O ano de nascimento foi preenchido incorretamente.')
            error = 1
        finally: #valid birth year input
            if error == 0:#case no error ocurred
                age = 2021-int(year)#calcular idade
                if int(year)>date.today().year:#check if filled year is not greater than current year
                    print(f'Hoje é {date.today().day:02}/{date.today().month:02}/{date.today().year}, o ano de nascimento foi preenchido incorretamente.')
                    pass
                else:    
                    if age<16:
                        print(f'\nVocê tem {age} anos.')
                        return False
                    elif age>=16 and age<18:
                        print(f'\nVocê tem {age} anos, o voto é OPCIONAL.')
                        return True
                    elif age>=18 and age<70:
                        print(f'\nVocê tem {age} anos, o voto é OBRIGATÓRIO.')
                        return True
                    else:
                        print(f'\nVocê tem {age} anos, o voto é OPCIONAL')
                        return True


def votacao():#election function
    votes.clear()#clear votes dict
    for c in range(len(candidates)):#loop to create valid index in votes dict
        votes[f'{candidates[c]}']=0
    while True:#loop to register one vote
        if autoriza_voto()!=True:
            print(f'\nVocê não pode votar.')
        else:
            print('\nEscolha seu candidato e vote no número respectivo a ele:')
            for c in range(len(candidates)):
                print(f'{(c+1):02} - {candidates[c]}')
            while True:
                vote = input('\nVoto: ')
                try:
                    int(vote)
                except:
                    print(f'\nOpção inválida, digite um número de 1 à {len(candidates)+1}.')
                finally:
                    if int(vote)>len(candidates):
                        print(f'\nOpção inválida, digite um número de 1 à {len(candidates)+1}.')
                    else:
                        break
            votes[f'{candidates[int(vote)-1]}']=(votes[f'{candidates[int(vote)-1]}']+1)
            print('\nVoto registrado.')
        if input(f'\nContinuar votação?[S/N]').upper()[0] == 'N':
            print(f'\nVotação encerrada.\n')
            break#end election
        else:
            print(f'\nPRÓXIMO ELEITOR\n')
    print(f'Candidato{" "*25}Votos')
    for c in range(len(candidates)):#loop for show election results
        print(f'{candidates[c]}{" "*(25+11-len(candidates[c]))}{votes[candidates[c]]}')
    winnerList=[]
    for c in range(len(candidates)):
        winnerList.append(votes[f'{candidates[c]}'])
        winnerIndex=winnerList.index(max(winnerList))
    print(f'\n{candidates[winnerIndex]} teve mais votos nessa eleição.')


print(f'{"="*25}DIA DE ELEIÇÃO{"="*25}') 
print(f'\n Se você tem 16 anos completos já tem o diretio a voto mas se tem menos que 18 anos ou 70 anos ou mais seu voto é opcional.\n')

votacao()