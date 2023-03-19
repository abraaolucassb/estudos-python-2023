"""
VERSÃO ANTIGA

print("Qual é o seu nome?")
nome = input()

print("Qual a sua idade?")
idade = input()

print("Bem-vindo(a) %s que tem %s anos." % (nome, idade))
"""

"""
VERSÃO ATUAL
print("Qual é o seu nome?")
nome = input()

print("Qual a sua idade?")
idade = input()

print("Bem vindo {0} que tem a idade de {1} anos!".format(nome, idade))
"""

# VERSÃO MAIS ATUAL
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

print(
    f"Bem vindo {nome} que tem a idade de {idade} anos, ou seja, nasceu em {2023 - idade}!")

print("oi")
