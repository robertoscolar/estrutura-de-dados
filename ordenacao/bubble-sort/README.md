# Bubble Sort

## Complexidade de Tempo (Big O)

| Caso                    | Complexidade | Descrição                                                                 |
|-------------------------|--------------|---------------------------------------------------------------------------|
| Melhor caso             | O(n)         | Quando a lista já está ordenada, é feita apenas uma passagem sem trocas.  |
| Caso médio              | O(n²)        | Combinações típicas de elementos exigem múltiplas trocas e comparações.   |
| Pior caso               | O(n²)        | Quando a lista está em ordem reversa, exige o máximo de trocas possíveis. |

## Complexidade de Espaço

- O(1) (in-place, apenas algumas variáveis extras são usadas)

---

## Explicação

O **Bubble Sort** é um algoritmo de ordenação simples que funciona comparando pares adjacentes de elementos em uma lista. Se os elementos estão fora de ordem, eles são trocados. Esse processo é repetido até que a lista esteja ordenada. O nome vem da ideia de que os elementos "maiores" vão "subindo" para o topo como bolhas na água.

Apesar de ser fácil de entender e implementar, o Bubble Sort é ineficiente para listas grandes devido à sua complexidade de tempo quadrática (O(n²)).

---

## Passo-a-passo

Aqui está como o Bubble Sort funciona passo-a-passo:

1. **Início do Processo**:
   - Comece pelo início da lista.
   - Compare o primeiro par de elementos adjacentes.

2. **Comparação e Troca**:
   - Se o elemento atual for maior que o próximo, troque-os de lugar.
   - Caso contrário, continue para o próximo par.

3. **Iteração Completa**:
   - Depois de passar por toda a lista, o maior elemento estará no final.
   - Ignore o último elemento na próxima iteração, pois ele já está ordenado.

4. **Repita o Processo**:
   - Continue iterando pela lista, ignorando progressivamente os elementos já ordenados.
   - Pare quando nenhuma troca for feita em uma passagem (a lista está ordenada).

---

## Exemplo Prático

Dada a lista: `[5, 3, 8, 6, 2]`

### Iterações:
1. **Primeira Passagem**:
   - `[5, 3, 8, 6, 2]` → Troca 5 e 3 → `[3, 5, 8, 6, 2]`
   - `[3, 5, 8, 6, 2]` → Não troca 5 e 8 → `[3, 5, 8, 6, 2]`
   - `[3, 5, 8, 6, 2]` → Troca 8 e 6 → `[3, 5, 6, 8, 2]`
   - `[3, 5, 6, 8, 2]` → Troca 8 e 2 → `[3, 5, 6, 2, 8]`

2. **Segunda Passagem**:
   - `[3, 5, 6, 2, 8]` → Não troca 3 e 5 → `[3, 5, 6, 2, 8]`
   - `[3, 5, 6, 2, 8]` → Não troca 5 e 6 → `[3, 5, 6, 2, 8]`
   - `[3, 5, 6, 2, 8]` → Troca 6 e 2 → `[3, 5, 2, 6, 8]`

3. **Terceira Passagem**:
   - `[3, 5, 2, 6, 8]` → Não troca 3 e 5 → `[3, 5, 2, 6, 8]`
   - `[3, 5, 2, 6, 8]` → Troca 5 e 2 → `[3, 2, 5, 6, 8]`

4. **Quarta Passagem**:
   - `[3, 2, 5, 6, 8]` → Troca 3 e 2 → `[2, 3, 5, 6, 8]`

5. **Fim do Processo**:
   - Lista final: `[2, 3, 5, 6, 8]` (ordenada).
  
---

## Quando usar?

Use o **Bubble Sort** apenas para:
   - Educação e aprendizado de algoritmos de ordenação.
   - Conjuntos de dados muito pequenos.

Para aplicações reais e listas maiores, prefira algoritmos mais eficientes, como **Merge Sort** ou **Quick Sort**.
