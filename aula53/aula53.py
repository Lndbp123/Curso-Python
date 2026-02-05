"""
enumerate - Enumerando iteráveis (índices)
"""

lista = ['Leonardo', 'Carol' , 'João', 'Maria'] 
lista.append("Dileides")

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))


for item in lista_enumerada:
    print(item)