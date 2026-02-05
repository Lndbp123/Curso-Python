"""
split e join com list e str
split - divide uma string em várias substrings a partir de um separador
join - une uma lista de strings em uma única string, usando um separador

"""



frase = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_frase = frase.split(' ')

for i, frase in enumerate(lista_frase):
    print(lista_frase[i].strip())

print(lista_frase)