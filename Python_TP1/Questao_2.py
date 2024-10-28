import random

def ordenar_cartas(cartas_embaralhadas):
    ordenado = []

    while cartas_embaralhadas:
        carta = cartas_embaralhadas.pop(0)
        
        if not ordenado:
            ordenado.append(carta)
        else:
            if carta == ordenado[0] - 1:
                ordenado.insert(0, carta)
            elif carta == ordenado[-1] + 1:
                ordenado.append(carta)
            else:
                cartas_embaralhadas.append(carta)

    return ordenado

cartas_embaralhadas = list(range(1, 14))
random.shuffle(cartas_embaralhadas)

print("Cartas embaralhadas:", cartas_embaralhadas)
cartas_ordenadas = ordenar_cartas(cartas_embaralhadas)
print("Cartas ordenadas:", cartas_ordenadas)
