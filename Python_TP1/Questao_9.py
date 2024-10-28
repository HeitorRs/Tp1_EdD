def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

casos = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 1, 4, 2, 8],
    [3, 0, 2, 5, -1, 4, 1],
    [5, 4, 3, 2, 1]
]

for index, caso in enumerate(casos):
    lista_ordenada = bubble_sort(caso.copy())
    print(f'Caso {index + 1}: Original: {caso}\n\tOrdenado: {lista_ordenada}')