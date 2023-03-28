"""
Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo que 
pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.
"""

idade = int(input('Qual sua idade? '))

if idade >= 18 and idade <= 67:
    print('Você está dentro da idade permitida. Você pode doar sangue!!')
elif idade < 18:
    print('Você está muito novo, ainda não pode doar sangue!')
elif idade > 67:
    print('Você está muito velho, não pode mais doar sangue!')
