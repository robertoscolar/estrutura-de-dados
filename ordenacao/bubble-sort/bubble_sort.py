import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n - 1):
            if lista[j] > lista[j+1]:
                variavel_auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = variavel_auxiliar

if __name__ == "__main__":
    lista = random.sample(range(1, 1000), 5)
    print(f"Lista Original: {lista}\n")
    bubble_sort(lista)
    print(f"Lista Ordenada: {lista}\n")