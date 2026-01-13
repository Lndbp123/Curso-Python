"""
Repetiçoes
while(enquanto)
executa um bloco de codigo enquanto
"""

condicao = True

while condicao:
    nome = input(f"Digite seu nome:")
    print(f"Seu nome é {nome}") 


    if nome == "sair":
        break

print("Acabou")