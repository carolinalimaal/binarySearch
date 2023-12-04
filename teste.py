import timeit as t

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

vetor = [1 for _ in range(50000000)]


tempo = t.timeit(lambda: pesquisa_binaria(vetor, 0), number=10000)

print(tempo)
