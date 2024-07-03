from random import randint
from time import sleep

print('\033[34m-='*20)
print('{:^40}' .format("Vamos jogar Jokenpô"))
print('\033[34m-=\033[m'*20)

escolha = str(input('\n\tQual você vai jogar? ')).upper().strip()

itens = ('PEDRA', 'PAPEL', 'TESOURA')

if escolha in itens:
    escolhacomp = randint(0, 2)
    computador = itens[escolhacomp]

    print()

    print(' '*10 + '\033[1m{}' .format('JO'), end='')
    sleep(0.5)
    print('KEN', end='')
    sleep(0.5)
    print('PÔ\033[m')
    sleep(0.5)

    print('\n\tEu escolho \033[1m{}\033[m'.format(computador.lower()))
    sleep(0.5)

    if escolha == computador:
        print('\n\tDeu \033[1;33mempate!\033[m :/'
              '\n\tVamos tentar outra vez?')
    elif (escolha == 'PEDRA' and computador == 'PAPEL') or (escolha == 'PAPEL' and computador == 'TESOURA') or (
            escolha == 'TESOURA' and computador == 'PEDRA'):
        print('\n\tQue pena, você \033[1;31mperdeu\033[m :('
              '\n\tMas não desista e tente outra vez')
    else:
        print('\n\tPARABÉNS você \033[1;32mganhou\033[m :D'
              '\n\tAceita me enfrentar de novo?')
else:
    print('\n\tParece que você digitou uma opção inválida'
          '\n\tTente novamente')
