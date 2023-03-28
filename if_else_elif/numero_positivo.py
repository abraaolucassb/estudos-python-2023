'''
Ler 1 número. Se positivo, imprimir raiz quadrada se não o quadrado. 
'''
from math import sqrt

numero = float(input('Digite um número: '))

if numero > 0:
    print('A raiz quadrada do seu número é ', sqrt(numero))
else:
    print('O quadrado do seu número é ', numero ** 2)
