import random

def numeros_aleatorios(nome_ficheiro, quantidade_numeros):
    with open(nome_ficheiro, 'w') as ficheiro:
        for i in range(quantidade_numeros):
            numero = random.randint(0,1000000)
            ficheiro.write(str(numero) + '\n')

def numeros_ordenados(nome_ficheiro_aleatorio, nome_ficheiro_ordenado):
    with open(nome_ficheiro_aleatorio, 'r') as ficheiros:
        numeros = [int(line.strip()) for line in ficheiros]
    numeros.sort()
    with open(nome_ficheiro_ordenado, 'w') as ficheiros:
        for numero in numeros:
            ficheiros.write(str(numero) + '\n')


quantidades = [100, 1000, 10000, 100000]

for quantidade in quantidades:
    nome_ficheiro_aleatorio = f'numeros_{quantidade}.txt'
    nome_ficheiro_ordenado = f'numeros_ordenados_{quantidade}.txt'
    numeros_aleatorios(nome_ficheiro_aleatorio, quantidade)
    numeros_ordenados(nome_ficheiro_aleatorio, nome_ficheiro_ordenado)