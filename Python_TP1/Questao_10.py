def bubble_sort_strings(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

casos = [
    ["banana", "maça", "laranja", "kiwi"],
    ["zebra", "mico", "lontra", "abacaxi", "uva"],
]

for index, ex in enumerate(casos):
    lista_ordenda = bubble_sort_strings(ex.copy())
    print(f'Caso {index + 1}:\tOriginal: {ex}\n\tOrdenado: {lista_ordenda}')