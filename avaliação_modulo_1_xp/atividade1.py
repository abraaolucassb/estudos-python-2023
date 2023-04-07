'''

1. Execute e analise a saída do seguinte código no Google Colab1.

inicio = 0
fim = 100

for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)
'''

'''
Altere o código da atividade 1 para que ele exiba os números múltiplos de
2, 5 e 7 (simultaneamente) e que estejam dentro do intervalo entre 100 e
500 (incluindo o 100 e o 500).

inicio = 100
fim = 500

for numero in range(inicio, fim):
    if numero % 5 == 0 and numero % 2 == 0 and numero % 7 == 0:
        print(numero)
'''

'''
Altere o código da atividade 1, criando uma variável divisor e, em seguida,
verifique quais os números no intervalo entre 0 e 1000 (incluindo o 0 e
excluindo o 1000) são múltiplos da variável divisor.

divisor = 7

for numero in range(0, 1000):
    if numero % divisor == 0:
        print(numero)
'''

# variáveis do tipo string

'''
. Crie um código declarando as seguintes variáveis do tipo
string:
# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'
Em seguida, realize as seguintes transformações nas variáveis:
● Transforme todos os caracteres das variáveis em maiúsculo;
● Transforme todos os caracteres das variáveis em minúsculo;
● Exiba a posição do caractere ã, se presente, em cada uma das variáveis;
● Exiba o número de caracteres de cada variável;
● Remova os pontos (.) e o hífen (–) da variável cpf.

nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

maisculo = [nome, cidade]

for i in range(len(maisculo)):
    maisculo[i] = maisculo[i].upper()

print(maisculo)

for i in range(len(maisculo)):
    maisculo[i] = maisculo[i].lower()

print(maisculo)

posicoes = []

for i in range(len(maisculo)):
    maisculo[i] = maisculo[i].lower()
    for j in range(len(maisculo[i])):
        if maisculo[i][j] == 'ã':
            posicoes.append(j)

print("Posições dos caracteres 'ã':", posicoes)

maisculo = [nome, cidade, cpf]

for i in range(len(maisculo)):
    tamanho = len(maisculo[i])
    print(f"A variável {maisculo[i]} tem {tamanho} caracteres.")

cpf_sem_pontos = cpf.replace('.', '').replace('-', '')

print(cpf_sem_pontos)
'''

'''
5. Crie um código que realize o somatório de todos os caracteres da seguinte
string:
numero = '127957'
Para resolver este problema, considere as seguintes dicas:
● A soma deverá ser 1 + 2 + 7 + 9 + 5 + 7 = 31;
● Utilize o laço de repetição for ... in; para percorrer cada caractere da string;
● Utilize a conversão do tipo
string para o tipo
inteiro (int(caractere)) para
converter os caracteres em valores numéricos;
● Utilize uma variável auxiliar, soma, para acumular o somatório dos valores.
'''

numero = '127957'
soma = 0

for i in numero:
    soma += int(i)
print(soma)
