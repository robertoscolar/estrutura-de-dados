import random

if __name__ == "__main__":
    lista = random.sample(range(1, 1000), 5)
    print(f"Lista Original: {lista}\n\n")
    selection_sort(lista)
    print(f"Lista Ordenada: {lista}\n\n")