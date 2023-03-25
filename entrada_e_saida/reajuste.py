'''
Receber um valor qualquer do teclado e imprimir esse valor com reajuste superior de 10%.
'''

valor = float(input('Digite um valor: '))
reajuste = int(input('Digite a porcentagem do reajuste: '))

novo_valor = valor + valor * reajuste / 100

print(f'O novo valor com o reajuste é: {novo_valor}')
