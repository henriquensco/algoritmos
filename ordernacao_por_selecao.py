#Busca o menor elemento dentro de um array
def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    
    return menor_indice

#Ordena do maior para o menor
def ordenacao_por_selecao(arr):
    novo_array = []

    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_array.append(arr.pop(menor))

    return novo_array



arr = [5, 6, 7, 8, 2]

#bus_menor = busca_menor(arr)

ord_selecao = ordenacao_por_selecao(arr)

print(ord_selecao)