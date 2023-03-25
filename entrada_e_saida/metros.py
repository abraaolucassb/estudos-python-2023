'''
Fazer um programa que pergunta um valor em metros e imprime o correspondente em decímetros, centímetros e milímetros.
'''

numero = float(input('Digite um número em metros: '))

mil = numero * 1000
cen = numero * 100
dec = numero * 10

print(
    f'O seu número em metros convertido para milímetros é {mil}.',
    f'\nO seu número convertido para centímetros é {cen}.',
    f'\nO seu número convertido para decímetros é {dec}.')
