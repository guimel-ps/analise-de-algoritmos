# Algoritmos Clássicos em Python

Implementação, simulação e análise de complexidade de três algoritmos fundamentais: multiplicação de matrizes, busca binária e busca linear com sentinela.

Cada script tem o código executável e, nos comentários, o desenvolvimento passo a passo do resultado e a análise de custo computacional.

## Estrutura

```
.
├── Q1.py   # Multiplicação matricial x soma matricial
├── Q2.py   # Busca binária
└── Q3.py   # Busca linear com sentinela
```

## Conteúdo

### Q1: Multiplicação de matrizes
- Multiplicação de uma matriz A (3x2) por B (2x2) com três laços aninhados.
- Resultado: `C = [[-4, -15], [-4, -3], [6, -6]]`
- Comparação de custo com a soma matricial: **O(n·m·p)** contra **O(n·m)**.

### Q2: Busca binária
- Busca da chave `5` em uma lista ordenada, exibindo cada passo (limites inferior/superior e índice do meio).
- Resultado: `(5, 5)`, encontrado em 4 passos.
- Complexidade: **O(log n)**.
- Análise de pontos de atenção na implementação: inicialização dos limites, índices fora da lista e retorno quando a chave não existe.

### Q3: Busca linear com sentinela
- Busca em uma lista heterogênea (números e strings) usando `append` da chave como sentinela.
- Retorna o índice da chave e os dois elementos seguintes.
- Demonstra o efeito colateral do `append` na lista original e o uso de `global`.
- Análise de uma condição de parada que nunca é atingida.

## Como executar

```bash
python Q1.py
python Q2.py
python Q3.py
```

Requer apenas Python 3, sem dependências externas.

## Saídas esperadas

```
# Q1
[[-4, -15], [-4, -3], [6, -6]]

# Q2
Resultado: (5, 5)

# Q3
(6, 'Inseto', 'Formiga')
(0, 'Ave', 'Galinha')
(3, 'Felino', 'Gato')
[1, 'Ave', 'Galinha', 5, 'Felino', 'Gato', 8, 'Inseto', 'Formiga', 8, 1, 5]
```

## Autor

**Miguel Silva Pereira**: estudante de Ciência de Dados, Fatec Baixada Santista.
