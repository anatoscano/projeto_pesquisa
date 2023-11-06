import time
import statistics
import matplotlib.pyplot as plt

def f_tempo(funcao, n,n_vezes):
    tempos = []
    for i in range(n_vezes):
        inicio = time.time()
        resultado = funcao(n)
        fim = time.time()
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)

    media = statistics.mean(tempos)
    desvio_padrao = statistics.stdev(tempos)

    return tempos, media, desvio_padrao

def f_boxplot(lista_tempos):
    plt.boxplot(lista_tempos)
    plt.show()

def f_complexidade(funcao, lista_n, n_vezes):
    dic_stats = {}
    dic_tempos = {}

    for n in lista_n:
        tempos, media, desvio_padrao = f_tempo(funcao, n, n_vezes)
        dic_stats[n] = (media, desvio_padrao)
        dic_tempos[n] = tempos
    return dic_stats, dic_tempos

def f_complexidade_boxplot(dic_tempos):
    for input, tempos in dic_tempos.items():
        f_boxplot(tempos)