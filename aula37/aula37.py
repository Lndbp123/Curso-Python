contador = 0

while contador < 100:
    contador += 1
    print(contador)

    if contador == 6:
        print("não vou mostrar o 6")
        continue
    print(contador)

    if contador ==100:
        break