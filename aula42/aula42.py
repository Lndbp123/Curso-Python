frase = 'O Python é uma linguagem de programação'\
        'multiparadigma.'\
        'Python foi criado por Guido van Rossum.'

i = 0
while i < len(frase):
    letra = frase[i]
    quantas_vezes = letra_apareceu = frase.count(letra)
    print(f'A letra "{letra}" apareceu {quantas_vezes} vezes na frase.')

    i += 1

