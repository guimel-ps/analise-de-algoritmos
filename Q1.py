# Q1 - multiplicação matricial x Soma matricial


A = [[5, 8], [1, 0], [2, 7]]
B = [[-4, -3], [2, 0]]
C = [[0, 0], [0, 0], [0, 0]]

for i in range(0, 3):
    for j in range(0, 2):
        C[i][j] = 0
        for k in range(0, 2):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

print("Matriz C = A x B:")
print(C)


# SIMULAÇÃO (cada C[i][j] = soma de A[i][k] * B[k][j], k = 0..1)
# C[0][0] = 5*(-4) + 8*2  = -20 + 16 = -4
# C[0][1] = 5*(-3) + 8*0  = -15 +  0 = -15
# C[1][0] = 1*(-4) + 0*2  =  -4 +  0 = -4
# C[1][1] = 1*(-3) + 0*0  =  -3 +  0 = -3
# C[2][0] = 2*(-4) + 7*2  =  -8 + 14 =  6
# C[2][1] = 2*(-3) + 7*0  =  -6 +  0 = -6

# RESULTADO: C = [[-4, -15], [-4, -3], [6, -6]]


# QUAL EXECUTA MAIS RÁPIDO?  A SOMA MATRICIAL


# Justificativa:
# - A soma faz UM laço duplo (linhas x colunas): cada elemento
#   exige 1 operação -> complexidade O(n*m).
# - A multiplicação tem TRÊS laços aninhados (i, j, k): cada
#   elemento de C exige várias multiplicações e somas ->
#   O(n*m*p), para matrizes quadradas O(n^3).
# - Neste exemplo: multiplicação = 3*2*2 = 12 multiplicações
#   + 12 somas; soma matricial = 3*2 = 6 somas.
# - Observação: A (3x2) e B (2x2) têm dimensões diferentes, então a
#   soma A+B não é definida de fato; a comparação é sobre o custo do
#   algoritmo (dois laços contra três laços).
