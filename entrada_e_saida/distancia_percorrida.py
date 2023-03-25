'''
Informe o tempo gasto numa viagem (em horas), a velocidade média e mostre a distância percorrida.
'''

tempo = float(input('Digite o tempo gasto em horas: '))
velo = int(input('Digite a velocidade média: '))

distancia = tempo * velo

print(f'A distância percorrida é {distancia} KM.')
