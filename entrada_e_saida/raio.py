"""
Escreva um programa que pergunte o raio de uma circunferência, e em seguida mostre o
diâmetro, comprimento e área da circunferência.
"""

raio = float(input("Qual o raio da circunferência?"))


pi = 3.14

diametro = raio * 2
comprimento = 2 * pi * raio
area = pi * raio**2


print(
    f"A sua circunferência tem raio de {raio} e:\nDiâmetro: {diametro}\nComprimento: {comprimento}\nÁrea: {area}")
