'''
Fazer um programa que solicita um número decimal e imprime o correspondente em hexa e octal.
'''

numero = int(input('Por favor, digite um número decimal: '))

hexa = hex(numero)
octa = oct(numero)

print(f"""O seu número decimal para hexa é: {hexa}
O seu número em octal é: {octa}""")
