def pesquisa_sequencial(lista,n):
    for item in lista:
        if item == n:
            return True
    return False

def pesquisa_sequencial_recursiva(lista,n):
    if not lista:
        return False
    if lista[0] == n:
        return True
    return pesquisa_sequencial_recursiva(lista[1:],n)

def pesquisa_binaria(lista,n):
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == n:
            return True
        elif n < lista[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
    return False

def pesquisa_binaria_recursiva(lista, n):
    if len(lista) == 0:
        return False
    else:
        meio = len(lista)//2
        if lista[meio] == n:
            return True
        else:
            if n < lista[meio]:
                return pesquisa_binaria_recursiva(lista[:meio],n)
            else:
                return pesquisa_binaria_recursiva(lista[meio+1:],n)
