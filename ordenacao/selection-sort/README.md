# Selection Sort

## Complexidade de Tempo (Big O)

| Caso                 | Complexidade | Descrição                                                                 |
|----------------------|--------------|---------------------------------------------------------------------------|
| Melhor caso          | O(n²)        | Sempre percorre a lista inteira para encontrar o menor elemento.          |
| Caso médio           | O(n²)        | O número de comparações é o mesmo em todos os casos.                      |
| Pior caso            | O(n²)        | Mesmo no pior caso, o número de comparações permanece constante.          |

---

## Explicação

O **Selection Sort** é um algoritmo simples de ordenação que divide a lista em duas partes: uma parte ordenada e outra não ordenada. Ele seleciona iterativamente o menor elemento da parte não ordenada e o move para o final da parte ordenada.

Embora seja fácil de implementar, ele não é eficiente para listas grandes devido à sua complexidade quadrática em todos os casos.

---

## Passo-a-passo

1. **Início do Processo**:
   - Divida a lista em duas partes: ordenada (inicialmente vazia) e não ordenada.

2. **Seleção do Menor Elemento**:
   - Percorra a lista não ordenada para encontrar o menor elemento.
   - Troque o menor elemento com o primeiro elemento da parte não ordenada.

3. **Repita o Processo**:
   - Expanda a parte ordenada e reduza a não ordenada.
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

