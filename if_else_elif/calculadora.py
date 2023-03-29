"""
Fazer uma calculadora simples com as quatro operações usando IF-ELSE-ELIF.
"""

import sys

option = int(input("""Escolha uma opção:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
>>> """))

if option < 1 or option > 4:
    print('Por favor, digite algo o número de algumas das opções.')
    sys.exit()

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o seguno número: '))

if option == 1:
    print('A adição é: ', numero1 + numero2)
elif option == 2:
    print('A subtração é: ', numero1 - numero2)
elif option == 3:
    print('A multiplicação é: ', numero1 * numero2)
else:
    print('A divisão é: ', numero1 / numero2)
