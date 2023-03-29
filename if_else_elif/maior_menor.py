'''
Faça um programa que receba três inteiros e diga qual deles é o maior e qual o menor.
'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'O {num1} é o maior dentre os três números!')
elif num1 < num3 and num1 < num3:
    print(f'O {num1} é o menor dentre os três números!')

if num2 > num3 and num2 > num1:
    print(f'O {num2} é o maior dentre os três números!')
elif num2 < num3 and num2 < num1:
    print(f'O {num2} é o menor dentre os três números!')

if num3 > num2 and num3 > num1:
    print(f'O {num3} é o maior dentre os três números!')
elif num3 < num2 and num3 < num1:
    print(f'O {num3} é o menor dentre os três números!')
