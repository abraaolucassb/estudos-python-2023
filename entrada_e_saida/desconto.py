'''
Informar um preço de um produto e calcular novo preço com desconto de 9%.
'''

preco_do_produto = float(input('Digite o valor do produto: '))

desconto = preco_do_produto - (9 * preco_do_produto / 100)

print(f'O produto que era R$ {preco_do_produto}, agora é {desconto}.')
