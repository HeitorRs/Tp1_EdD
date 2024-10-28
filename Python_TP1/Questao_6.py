def encontrar_quadrado(graos):
    quadrado = 1
    graos_no_quadrado = 1

    while graos > graos_no_quadrado:
        quadrado += 1
        graos_no_quadrado *= 2

    return quadrado

graos = 128
print(encontrar_quadrado(graos))