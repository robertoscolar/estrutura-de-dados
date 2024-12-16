# Merge Sort

## Complexidade de Tempo (Big O)

| Caso                 | Complexidade | Descrição                                                                 |
|----------------------|--------------|---------------------------------------------------------------------------|
| Melhor caso          | O(n log n)   | Mesmo se os dados já estiverem ordenados, o algoritmo executa as divisões e fusões. |
| Caso médio           | O(n log n)   | A divisão dos dados e a fusão das sublistas têm complexidade \(O(n \log n)\). |
| Pior caso            | O(n log n)   | A complexidade é a mesma no pior caso, pois o algoritmo sempre divide e funde as sublistas da mesma forma. |

## Complexidade de Espaço

- O(n) (necessário espaço extra para armazenar as sublistas temporárias).

---

## Explicação

**Merge Sort** é um algoritmo de ordenação baseado no paradigma de **dividir e conquistar**. Ele divide a lista em duas metades recursivamente até que cada sublista tenha um único elemento. Em seguida, ele começa a **fundir** essas sublistas, sempre mantendo a ordenação.

- **Estável**: O **Merge Sort** é estável, o que significa que ele preserva a ordem de elementos iguais.
- **Eficiência**: A complexidade \(O(n \log n)\) é garantida, tanto no melhor quanto no pior caso.
- **Exigente em memória**: Como requer espaço extra para as sublistas temporárias, o **Merge Sort** não é ideal para ambientes com memória limitada.

---

## Passo-a-passo

1. **Divisão**:
   - A lista é recursivamente dividida ao meio até que cada sublista tenha um único elemento.

2. **Fusão**:
   - Duas sublistas ordenadas são fundidas em uma única lista ordenada, comparando-se os elementos das sublistas e colocando-os na ordem correta.

3. **Recursão**:
   - Esse processo de divisão e fusão continua até que toda a lista esteja ordenada.

---

## Exemplo Prático

Dada a lista: `[5, 3, 8, 6, 2]`

### Iterações:
1. **Divisão**:
   - Divida a lista em duas sublistas: `[5, 3]` e `[8, 6, 2]`.

2. **Divisão Recursiva**:
   - Divida `[5, 3]` em `[5]` e `[3]`, e depois funde para `[3, 5]`.
   - Divida `[8, 6, 2]` em `[8]` e `[6, 2]`, e depois divida `[6, 2]` em `[6]` e `[2]`, fundindo para `[2, 6]`. Assim, `[8, 6, 2]` se torna `[2, 6, 8]`.

3. **Fusão Final**:
   - Agora funde `[3, 5]` e `[2, 6, 8]` para formar `[2, 3, 5, 6, 8]`.

4. **Fim do Processo**:
   - Lista final: `[2, 3, 5, 6, 8]` (ordenada).

---

## Quando usar?

Use o **Merge Sort** para:

  - **Grandes listas**: Quando você precisa de um algoritmo estável e com desempenho garantido **O(n log n)**.
  - **Estabilidade**: Quando a estabilidade da ordenação é importante (elementos iguais devem manter sua ordem relativa).
  - **Listas grandes ou externas**: Para conjuntos de dados que não cabem na memória principal (algumas implementações de Merge Sort são usadas em algoritmos de ordenação externa, como em arquivos).

## Quando evitar?

  - **Espaço limitado**: O Merge Sort requer **O(n)** de espaço extra, o que pode ser um problema em ambientes com memória limitada.
  - **Listas pequenas**: Para listas pequenas, outros algoritmos como Insertion Sort ou Quick Sort podem ser mais eficientes devido ao seu menor overhead.

---

## Vantagens

  - **Estabilidade**: O Merge Sort é estável, ou seja, preserva a ordem dos elementos iguais.
  - **Complexidade garantida**: O tempo de execução é sempre **O(n log n)**, tanto no melhor quanto no pior caso.
  - **Usado em ordenação externa**: Ideal para ordenar grandes quantidades de dados que não podem ser carregados completamente na memória RAM.

## Desvantagens

  - **Espaço adicional**: Requer espaço extra para armazenar as sublistas temporárias durante o processo de fusão.
  - **Custo em memória**: Pode não ser a melhor escolha quando o uso de memória é uma preocupação.
