# Heap Sort

## Complexidade de Tempo (Big O)

| Caso                 | Complexidade | Descrição                                                                 |
|----------------------|--------------|---------------------------------------------------------------------------|
| Melhor caso          | O(n log n)   | O heap é construído e ajustado eficientemente, independentemente da ordem inicial. |
| Caso médio           | O(n log n)   | A construção do heap e as operações de remoção têm custo logarítmico.    |
| Pior caso            | O(n log n)   | Mesmo com os dados em ordem reversa, o heap é ajustado eficientemente.   |

## Complexidade de Espaço

- O(1) (in-place, usando apenas o espaço extra necessário para variáveis).

---

## Explicação

O **Heap Sort** é um algoritmo de ordenação baseado em árvores binárias (heaps). Ele utiliza a estrutura de um **Heap Máximo**, onde o maior elemento está na raiz. O algoritmo funciona ao construir um heap, remover iterativamente o maior elemento e reconstruir o heap até que a lista esteja ordenada.

É eficiente e possui uma complexidade de tempo garantida de \(O(n \log n)\), tornando-o adequado para listas grandes. Além disso, é **in-place**, o que significa que não requer memória adicional significativa.

---

## Passo-a-passo

1. **Construção do Heap**:
   - Construa um **Heap Máximo** a partir da lista, garantindo que o maior elemento esteja na raiz.

2. **Troca e Ajuste**:
   - Troque o maior elemento (raiz) com o último elemento da lista não ordenada.
   - Reduza o tamanho do heap e ajuste para restaurar a propriedade do heap.

3. **Repita o Processo**:
   - Continue até que todos os elementos tenham sido processados.

---

## Exemplo Prático

Dada a lista: `[5, 3, 8, 6, 2]`

### Iterações:
1. **Construção do Heap Máximo**:
   - Transforme a lista em um heap: `[8, 6, 5, 3, 2]`.

2. **Primeira Troca**:
   - Troque o maior elemento (`8`) com o último (`2`): `[2, 6, 5, 3, 8]`.
   - Ajuste o heap: `[6, 3, 5, 2, 8]`.

3. **Segunda Troca**:
   - Troque o maior elemento (`6`) com o penúltimo (`2`): `[2, 3, 5, 6, 8]`.
   - Ajuste o heap: `[5, 3, 2, 6, 8]`.

4. **Terceira Troca**:
   - Troque o maior elemento (`5`) com o terceiro (`2`): `[2, 3, 5, 6, 8]`.
   - Ajuste o heap: `[3, 2, 5, 6, 8]`.

5. **Quarta Troca**:
   - Troque o maior elemento (`3`) com o segundo (`2`): `[2, 3, 5, 6, 8]`.

6. **Fim do Processo**:
   - Lista final: `[2, 3, 5, 6, 8]` (ordenada).

---

## Quando usar?

Use o **Heap Sort** para:

  - Dados grandes que precisam de um algoritmo eficiente e estável em **O(n log n)**.
  - Cenários em que a memória é limitada, já que o Heap Sort é **in-place**.

Para listas pequenas, considere algoritmos mais simples como **Insertion Sort**.
