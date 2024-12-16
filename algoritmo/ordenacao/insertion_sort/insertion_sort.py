import random

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = key

#Execute
if __name__ == "__main__":
    lista = random.sample(range(1, 1000), 5)
    print(f"Lista Original: {lista}\n")
    insertion_sort(lista)
    print(f"Lista Ordenada: {lista}\n")