# Insertion Sort

## Complexidade de Tempo (Big O)

| Caso                 | Complexidade | Descrição                                                                 |
|----------------------|--------------|---------------------------------------------------------------------------|
| Melhor caso          | O(n)         | Quando a lista já está ordenada, apenas compara e insere elementos.       |
| Caso médio           | O(n²)        | Combinações típicas exigem múltiplos deslocamentos e inserções.           |
| Pior caso            | O(n²)        | Quando a lista está em ordem reversa, exige o máximo de deslocamentos.    |

## Complexidade de Espaço

- O(1) (in-place, apenas algumas variáveis extras são usadas)

---

## Explicação

O **Insertion Sort** é um algoritmo simples e intuitivo que constrói a lista ordenada de forma incremental. Ele percorre a lista de dados e, para cada elemento, o insere na posição correta dentro da parte ordenada da lista.

Ele é eficiente para conjuntos pequenos de dados ou listas que já estão quase ordenadas, mas é ineficiente para listas grandes devido à complexidade quadrática em seu caso médio e pior caso.

---

## Passo-a-passo

1. **Início do Processo**:
   - Considere que o primeiro elemento já está ordenado.
   - Escolha o próximo elemento da lista não ordenada.

2. **Comparação e Inserção**:
   - Compare o elemento atual com os elementos da lista ordenada.
   - Mova os elementos maiores para a direita para abrir espaço.

3. **Repita o Processo**:
   - Insira o elemento na posição correta.
   - Continue até que todos os elementos tenham sido processados.

---

## Exemplo Prático

Dada a lista: `[5, 3, 8, 6, 2]`

### Iterações:
1. **Primeira Passagem**:
   - Elemento atual: `3`
   - Lista ordenada: `[5]`
   - Insere `3` antes de `5`: `[3, 5, 8, 6, 2]`

2. **Segunda Passagem**:
   - Elemento atual: `8`
   - Lista ordenada: `[3, 5]`
   - `8` já está na posição correta: `[3, 5, 8, 6, 2]`

3. **Terceira Passagem**:
   - Elemento atual: `6`
   - Lista ordenada: `[3, 5, 8]`
   - Move `8` para a direita e insere `6`: `[3, 5, 6, 8, 2]`

4. **Quarta Passagem**:
   - Elemento atual: `2`
   - Lista ordenada: `[3, 5, 6, 8]`
   - Move todos os elementos maiores para a direita e insere `2`: `[2, 3, 5, 6, 8]`

5. **Fim do Processo**:
   - Lista final: `[2, 3, 5, 6, 8]` (ordenada).

---

# Quando usar

Use o **Insert Sort** apenas para:

  - Listas pequenas.
  - Dados quase ordenados.
  - Cenários onde simplicidade e clareza do algoritmo são mais importantes que eficiência.

Para aplicações reais e listas maiores, prefira algoritmos mais eficientes, como **Merge Sort** ou **Quick Sort**.
