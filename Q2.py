# Q2 - Busca binária

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(L)


def busca_bin(x):
    for p in range(1):
        posicao_inferior = 1
        posicao_superior = n
        passo = 0
        while posicao_inferior <= posicao_superior or posicao_superior == 0:
            meio = int((posicao_inferior + posicao_superior) / 2)
            passo += 1
            print(f"Passo {passo}: inferior={posicao_inferior}, "
                  f"superior={posicao_superior}, meio={meio}, L[meio]={L[meio]}")
            if L[meio] == x:
                return meio, L[meio]
                # (as linhas abaixo da prova nunca executam, pois há return antes)
                posicao_inferior = posicao_superior + 1
            else:
                if L[meio] < x:
                    posicao_inferior = meio + 1
                else:
                    posicao_superior = meio - 1


print("Resultado:", busca_bin(5))


# SIMULAÇÃO para x = 5  (n = 11)
# Passo 1: inferior=1, superior=11 -> meio=6, L[6]=6 > 5 -> superior = 5
# Passo 2: inferior=1, superior=5  -> meio=3, L[3]=3 < 5 -> inferior = 4
# Passo 3: inferior=4, superior=5  -> meio=4, L[4]=4 < 5 -> inferior = 5
# Passo 4: inferior=5, superior=5  -> meio=5, L[5]=5 == 5 -> RETORNA (5, 5)

# RESULTADO: (5, 5) posição 5, valor 5 (chave encontrada em 4 passos)

# COMPLEXIDADE MAIS ADEQUADA: O(log n)
# A cada passo o intervalo de busca cai pela metade, então no pior
# caso são cerca de log2(n) comparações (log2(11) ≈ 3,5 -> até 4 passos).
# Melhor caso: O(1) (chave no meio na 1ª tentativa).
# Requisito: a lista precisa estar ORDENADA.


