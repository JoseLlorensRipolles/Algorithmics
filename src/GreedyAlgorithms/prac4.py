import numpy as np
import math

def create_graph(N, maxvalue=1000):
    G = np.random.randint(maxvalue, size=(N, N))
    for i in range(N):
        G[i][i] = 0
    return G


def process_graph(G):
    N = G.shape[0]
    for i in range(N):
        for j in range(i+1, N):
            if G[i][j] > G[j][i]:
                G[i][j] -= G[j][i]
                G[j][i] = 0
            else:
                G[j][i] -= G[i][j]
                G[i][j] = 0
    return G


def generate_random_ordering(G):
    # let's assume that G is a square Numpy matrix of integers
    N = G.shape[0]
    return np.random.permutation(N)


def evaluate_greedy(G, ordering, j):
    N = G.shape[0]
    res = 0
    for i in range(N):
        if i in ordering:
            res += G[i][j]
            res -= G[j][i]
        else:
            res += G[j][i]
            res -= G[i][j]

    return res


def generate_greedy_ordering(G):
    # let's assume that G is a square Numpy matrix of integers
    N = G.shape[0]
    # EJERCICIO 1
    vertex_list = []
    for i in range(N):
        maximum = -math.inf
        index = -1
        for j in range(N):
            if j not in vertex_list:
                value = evaluate_greedy(G, vertex_list, j)
                if value > maximum:
                    maximum = value
                    index = j
        print(maximum)
        vertex_list.append(index)

    return vertex_list

def generate_greedy_ordering_opt(G):
    # let's assume that G is a square Numpy matrix of integers
    N = G.shape[0]
    # EJERCICIO 3
    vertex_list = []
    vertex_scores = []
    for i in range(N):
        vertex_scores.append(evaluate_greedy(G, [], i))

    for i in range(N):
        max = -math.inf
        index = -1
        for j in range(N):
            if j not in vertex_list:
                if vertex_scores[j] > max:
                    max = vertex_scores[j]
                    index = j
        vertex_list.append(index)

        for j in range(N):
            if j not in vertex_list:
                vertex_scores[j] -= G[j][index]
                vertex_scores[j] += G[index][j]
    return vertex_list


def evaluate(G, ordering):
    # assume that G.shape is of type (N,N) and ordering.shape is of type
    # (N) and is a permutation of values 0,...,N-1
    N = G.shape[0]
    return sum(G[ordering[i]][ordering[j]] - G[ordering[j]][ordering[i]]
               for i in range(N) for j in range(i + 1, N))


def show_evaluate(G, ordering):
    N = G.shape[0]
    positivos = list(G[ordering[i]][ordering[j]] for i in range(N) for j in range(i + 1, N))
    negativos = list(G[ordering[j]][ordering[i]] for i in range(N) for j in range(i + 1, N))
    vpos = sum(positivos)
    vneg = sum(negativos)
    resul = vpos - vneg
    print("(" + ",".join(map(str, positivos)) + ") - (" + ",".join(map(str, negativos)) +
          ") = ", vpos, "-", vneg, "=", resul)
    return resul


# si pruebas con este grafo:
G = np.asarray([[0, 8, 3, 2, 9],
                [3, 0, 3, 8, 2],
                [0, 2, 0, 6, 2],
                [4, 4, 8, 0, 0],
                [7, 7, 6, 2, 0]], dtype=np.int)
# el algoritmo voraz hace estos pasos:
# [] [(8, 0), (-5, 1), (-10, 2), (-2, 3), (9, 4)]
# [4] [(4, 0), (5, 1), (-2, 2), (2, 3)]
# [4, 1] [(-6, 0), (0, 2), (10, 3)]
# [4, 1, 3] [(-2, 0), (4, 2)]
# [4, 1, 3, 2] [(-8, 0)]
# y termina dando como resultado:
# [4, 1, 3, 2, 0]
# con valor 10

# este trozo prueba ejemplos aleatorios:
# N = 30
# G = create_graph(N, 100)
# print("G=",G)
G = process_graph(G)
print(G)
random_ordering = generate_random_ordering(G)
greedy_ordering = generate_greedy_ordering(G)
greedy_ordering = generate_greedy_ordering_opt(G)
print("random", evaluate(G, random_ordering))
print("greedy", evaluate(G, greedy_ordering))
