import time as t

tempoInicial = t.time()

def pesquisa_binaria(A, item):
    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return -1

vetor = [1 for _ in range(100000000)]

pesquisa_binaria(vetor, 0)

tempoFinal = t.time()

print(f'{tempoFinal - tempoInicial}')