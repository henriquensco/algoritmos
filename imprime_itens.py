from time import sleep

def imprime_itens(lista):
    for l in lista:
        sleep(1)
        print(l)


lista = [2, 4, 6, 8]
imprime_itens(lista)