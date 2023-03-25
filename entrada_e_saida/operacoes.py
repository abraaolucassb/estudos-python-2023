'''
Fazer um programa que solicite 2 números e informe:
-A soma dos números;
-O produto do primeiro número pelo quadrado do segundo;
-O quadrado do primeiro número;
-A raiz quadrada da soma dos quadrados;
-O seno da diferença do primeiro número pelo  segundo;
-O módulo do primeiro número.
'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2
prod = num1 * num2**2
quad = num1**2
raiz = (num1**2) + (num2**2) / 2
mod = abs(num1)

print(f'A soma entre os números: {soma}',
      f'\nO produto do primeiro pelo quadrado do segundo: {prod}',
      f'\nO quadrado do segundo: {quad}',
      f'\nA raiz da soma das raízes: {raiz}',
      f'\nO módulo do primeiro número: {mod}')
