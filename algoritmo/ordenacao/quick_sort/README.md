# Quick Sort

## Complexidade de Tempo (Big O)

| Caso                 | Complexidade | Descrição                                                                 |
|----------------------|--------------|---------------------------------------------------------------------------|
| Melhor caso          | O(n log n)   | Quando o pivô divide a lista de forma equilibrada em cada iteração.       |
| Caso médio           | O(n log n)   | A divisão da lista é relativamente equilibrada, resultando em uma boa performance. |
| Pior caso            | O(n²)        | Quando o pivô é sempre o menor ou maior elemento, resultando em divisões desequilibradas. |

## Complexidade de Espaço

- O(log n) (em média, devido à recursão, mas pode chegar a O(n) no pior caso se a pilha de chamadas for muito profunda).

---

## Explicação

O **Quick Sort** é um dos algoritmos mais eficientes e amplamente usados para ordenação. Ele utiliza o paradigma de **dividir e conquistar**: seleciona um elemento da lista como pivô e particiona a lista em duas sublistas, uma com elementos menores que o pivô e outra com elementos maiores. O algoritmo então aplica recursivamente o mesmo processo às sublistas.

- **Eficiência**: No melhor e caso médio, tem complexidade \(O(n \log n)\), mas no pior caso, onde a escolha do pivô é ruim, pode chegar a \(O(n^2)\).
- **In-place**: Não requer espaço adicional para armazenar elementos, o que o torna eficiente em termos de memória.

---

## Passo-a-passo

1. **Escolha do Pivô**:
   - Selecione um elemento da lista como pivô. Existem várias estratégias para isso, como escolher o primeiro, o último ou o elemento do meio.

2. **Particionamento**:
   - Reorganize os elementos da lista de modo que todos os elementos menores que o pivô fiquem à esquerda e todos os elementos maiores fiquem à direita.

3. **Recursão**:
   - Recursivamente, aplique o processo de ordenação às sublistas à esquerda e à direita do pivô.

4. **Repetir**:
   - Repita até que a lista inteira esteja ordenada.

---

## Exemplo Prático

Dada a lista: `[5, 3, 8, 6, 2]`

### Iterações:
1. **Escolha do Pivô**:
   - Pivô escolhido: `5` (pode ser o primeiro, o último ou qualquer outro critério de escolha).
   
2. **Particionamento**:
   - Organize os elementos em relação ao pivô: `[3, 2, 5, 6, 8]`.
   - Pivô `5` está na posição correta.

3. **Recursão**:
   - Sublista à esquerda de `5`: `[3, 2]`
   - Sublista à direita de `5`: `[6, 8]`

4. **Sublistas**:
   - Para a sublista `[3, 2]`, o pivô é `3`, a lista se torna `[2, 3]`.
   - Para a sublista `[6, 8]`, o pivô é `6`, a lista se torna `[6, 8]`.

5. **Fim do Processo**:
   - Lista final: `[2, 3, 5, 6, 8]` (ordenada).

---

## Quando usar?

Use o **Quick Sort** para:
- **Grandes listas**: Quando a performance é crucial e você precisa de um algoritmo eficiente.
- **Espaço limitado**: O **Quick Sort** é **in-place**, ou seja, não requer espaço extra proporcional ao tamanho dos dados.
- **Casos médios**: Quando o caso médio \(O(n \log n)\) é aceitável e você não se importa com o pior caso ocasional.
- **Algoritmos em tempo real**: Para cenários onde o tempo de execução é um fator importante, devido à sua boa média de desempenho.

### Quando evitar:
- **Listas pequenas**: Para listas pequenas, outros algoritmos como **Insertion Sort** podem ser mais eficientes devido ao menor overhead.
- **Necessidade de estabilidade**: O **Quick Sort** não é estável por padrão. Se precisar de estabilidade na ordenação (onde elementos iguais mantêm sua ordem original), use **Merge Sort** ou **Insertion Sort**.

---

## Otimização da Escolha do Pivô

Para evitar o pior caso (O(n²)), a escolha do pivô é crucial. Algumas estratégias de otimização incluem:

1. **Pivô Aleatório**:
   - Escolher um pivô aleatoriamente pode ajudar a reduzir a probabilidade de ocorrerem divisões desequilibradas.

2. **Pivô mediano de três**:
   - Selecionar o pivô como o valor mediano entre o primeiro, o último e o elemento do meio.
