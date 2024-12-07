import random

def selection_sort(lista):
    n = len(lista)
    for i in range(n-1):
        min_index = i
        
        for j in range(i, n):
            if lista[j] < lista[min_index]:
                min_index = j
        
        if lista[i] > lista[min_index]:
            variavel_auxiliar = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = variavel_auxiliar 

if __name__ == "__main__":
    lista = random.sample(range(1, 1000), 5)
    print(f"Lista Original: {lista}\n")
    selection_sort(lista)
    print(f"Lista Ordenada: {lista}\n")