# Selection Sort

## Complexidade de Tempo (Big O)

| Caso                 | Complexidade | Descrição                                                                 |
|----------------------|--------------|---------------------------------------------------------------------------|
| Melhor caso          | O(n²)        | Sempre percorre a lista inteira para encontrar o menor elemento.          |
| Caso médio           | O(n²)        | O número de comparações é o mesmo em todos os casos.                      |
| Pior caso            | O(n²)        | Mesmo no pior caso, o número de comparações permanece constante.          |

## Complexidade de Espaço

- O(1) (in-place, apenas algumas variáveis extras são usadas)

---

## Explicação

O **Selection Sort** é um algoritmo simples de ordenação que percorre repetidamente a lista para selecionar o menor elemento na parte não ordenada e trocá-lo com o primeiro elemento da parte não ordenada. A cada iteração, a parte ordenada da lista cresce e a parte não ordenada diminui até que toda a lista esteja ordenada.

Embora seja fácil de implementar e tenha uma estrutura simples, o algoritmo não é eficiente para listas grandes devido à sua complexidade quadrática em todos os casos, já que ele realiza comparações desnecessárias, mesmo quando a lista já está parcialmente ordenada.

---

## Passo-a-passo

1. **Início do Processo**:
   - O algoritmo começa na primeira posição da lista, considerando a parte não ordenada como toda a lista inicial.

2. **Seleção do Menor Elemento**:
   - Percorra a parte não ordenada da lista para encontrar o menor elemento.
   - Troque o menor elemento com o primeiro elemento da parte não ordenada.

3. **Repita o Processo**:
   - A cada iteração, o alcance da parte não ordenada diminui e a parte ordenada cresce.
   - Continue até que toda a lista esteja ordenada.

---

## Exemplo Prático

Dada a lista: `[5, 3, 8, 6, 2]`

### Iterações:
1. **Primeira Passagem**:
   - Lista não ordenada: `[5, 3, 8, 6, 2]`
   - Menor elemento: `2`
   - Troca `2` com `5`: `[2, 3, 8, 6, 5]`

2. **Segunda Passagem**:
   - Lista não ordenada: `[3, 8, 6, 5]`
   - Menor elemento: `3`
   - `3` já está na posição correta: `[2, 3, 8, 6, 5]`

3. **Terceira Passagem**:
   - Lista não ordenada: `[8, 6, 5]`
   - Menor elemento: `5`
   - Troca `5` com `8`: `[2, 3, 5, 6, 8]`

4. **Quarta Passagem**:
   - Lista não ordenada: `[6, 8]`
   - Menor elemento: `6`
   - `6` já está na posição correta: `[2, 3, 5, 6, 8]`

5. **Fim do Processo**:
   - Lista final: `[2, 3, 5, 6, 8]` (ordenada).

---

## Quando usar?

Use o **Selection Sort** para:

  - Listas pequenas.
  - Quando o custo de troca de elementos não é relevante.
  - Casos onde simplicidade e clareza do algoritmo são mais importantes que eficiência.

Para listas grandes, prefira algoritmos mais eficientes, como **Heap Sort**, **Merge Sort** ou **Quick Sort**.

