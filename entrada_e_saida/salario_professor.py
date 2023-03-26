'''
Calcule o salário líquido de um professor. Será fornecido valor da hora aula, 
o número de aulas dadas e a % de desconto do INSS sobre o valor bruto do salário.
'''

hora_aula = float(input('Qual o valor da hora-aula? '))
numero_aulas = float(input('Digite o número de aulas do professor no mês: '))
porcentagem = float(input('Qual a porcentagem de desconto do INSS? '))

salario_liquido = hora_aula * numero_aulas

salario_bruto = salario_liquido - (porcentagem * salario_liquido / 100)

print(f'O salário do professor é: {salario_bruto}')
