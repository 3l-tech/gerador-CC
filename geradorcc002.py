#bibliotecas
import random
from datetime import date
#variaveis
con = bin = 0
data = date.today().year
#layout
print('-' *43)
print(' Gerador CC  V2.0')
print('-' *43)
print(' [1] - VISA')         
print(' [2] - MASTER')
print(' [3] - BIN')
print(' TELEGRAM: @devrckm')
print('-' *43)
#Estruturas
while True:
    op = int(input(' Digite uma das opções: '))
    cvv = random.randrange(1,999)
    mes = random.randint(1,12)
    ano = data + random.randint(1,7)
    cc = random.randrange(1,9999999999)
    if op == 1:
        bin = 407347
        con += 1
        print('-' * 43)
        print('')
        print(' CC VISA GERADO #{}'.format(con))
        print('')
        print(' Cartão: {}{}'.format(bin, cc))
        print(' Cvv: {}'.format(cvv))
        print(' Validade: mês {} de {}'.format(mes, ano))
        print('-' *43)
    elif op == 2: 
        bin = 545805
        con += 1
        print('-' * 43)
        print('')
        print(' CC MASTER GERADO #{}'.format(con))
        print('')
        print(' Cartão: {}{}'.format(bin, cc))
        print(' Cvv: {}'.format(cvv))
        print(' Validade: mês {} de {}'.format(mes, ano))
        print('-' *43)
    elif op == 3:
        bin = int(input(' Insira uma bin de 06 dígitos:'))
        con += 1
        print('-' * 43)
        print('')
        print(' BIN GERADO #{}'.format(con))
        print('')
        print(' Cartão: {}{}'.format(bin, cc))
        print(' Cvv: {}'.format(cvv))
        print(' Validade: mês {} de {}'.format(mes, ano))
        print('-' *43)
    elif op < 1:
        print('')
        print('Gerador encerrado com sucesso!')
        print('')
        break
    else:
        print('-' * 43)
        print('Erro! Digite novamente!')
        print('-' *43)
    print('As Melhores CCs geradas estão aqui!')
    print('')