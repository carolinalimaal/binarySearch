import time as t

inicial = t.time()

def binarySearchIterative(array, value):
    begin = 0 # Index inicial do vetor
    end = len(array) - 1 # Index final do vetor

    while begin <= end: # Laço que determina a condição de parada da busca

        middle = (begin + end) // 2 # Calcula o meio do vetor

        if value == array[middle]: # Melhor caso: o valor buscado está no meio do vetor
            return middle, 'Valor encontrado' # Valor encontrado

        # Caso contrário, continua a busca na direita ou na esquerda do vetor
        if value > array[middle]: # Caso o valor buscado seja maior que o meio do vetor
            begin = middle + 1 # Index inicial agora passa a ser o meio + 1

        else: # Caso o valor buscado seja menor que o meio do vetor
            end = middle - 1 # Index final passa a ser o meio - 1

    return -1, 'Valor não encontrado no vetor' # Pior caso: o valor buscado não estar no vetor


vetor = [1 for _ in range(5000)]

test = binarySearchIterative(vetor, 0)

final = t.time()

print(test)
print(f'{(final - inicial):.20f}')
