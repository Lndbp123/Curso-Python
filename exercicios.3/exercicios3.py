"""
Peça ao usuario para digitar seu nome completo.
Peça ao usuario para digitar sua idade
se nome e idade forem digitados:

exiba
Seu nome é {nome}
Seu nome invetido é {nome invertido}
se nome contem ou não espaços
sei nome tem {n} letras
a primeira letra do nome é {letra}
a ultima letra do nome é {letra}
se nada for diigtado em nome ou idade, exiba "Desculpe, você deixou campos vazios."
"""
nome_usuario = input('Digite seu nome completo: ' )
idade_usuario = input('Digite sua idade: ')

if nome_usuario and idade_usuario:
    print(f"Seu nome é {nome_usuario}")
    print(f'Seu nome invertido é {nome_usuario[::-1]}')
    if '' in nome_usuario:
        print(f'Seu nome contem espaços')
    elif ''not in nome_usuario:
        print(f"Seu nome não contem espaços")
    print(f'Seu nome tem {len(nome_usuario.replace(" ", ""))} letras')
    print(f"A primeira letra do seu nome é {nome_usuario[0]}")
    print(f"A ultima letra do seu nome é {nome_usuario[-1]}")

else:
    print("Desculpe, você deixou campos vazios.")