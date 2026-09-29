# QUESTÃO 3 - Busca linear com sentinela

L = [1, "Ave", "Galinha", 5, "Felino", "Gato", 8, "Inseto", "Formiga"]
n = len(L)


def busca_linear(x):
    for p in range(1):
        L.append(x)
        global n
        n = n + 1
        i = 0
        while L[i] != x:
            i = i + 1
        if i != n + 1:
            return i, L[i + 1], L[i + 2]
        else:
            return "sem a chave"


print(busca_linear(8))
print(busca_linear(1))
print(busca_linear(5))
print(L)


# RESULTADO NO CONSOLE:
# (6, 'Inseto', 'Formiga')
# (0, 'Ave', 'Galinha')
# (3, 'Felino', 'Gato')
# [1, 'Ave', 'Galinha', 5, 'Felino', 'Gato', 8, 'Inseto', 'Formiga', 8, 1, 5]

# EXPLICAÇÃO:
# Lista inicial (n = 9): índices 0:1, 1:Ave, 2:Galinha, 3:5, 4:Felino,
#                        5:Gato, 6:8, 7:Inseto, 8:Formiga
# - busca_linear(8): faz append(8), n=10; o primeiro 8 está no índice 6
#   retorna (6, L[7], L[8]) = (6, 'Inseto', 'Formiga')
# - busca_linear(1): append(1), n=11; o 1 está no índice 0
#   retorna (0, L[1], L[2]) = (0, 'Ave', 'Galinha')
# - busca_linear(5): append(5), n=12; o 5 está no índice 3
#   retorna (3, L[4], L[5]) = (3, 'Felino', 'Gato')
# - print(L): a lista ficou com os 3 valores adicionados no final
#   (8, 1, 5), pois o append altera a lista original.

