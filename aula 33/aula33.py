"""Faça um programa que peça ao usuario para digitar um numero inteiro, 
informe se este numero e par ou impar.
Caso o usuario não digite um numero inteiro, informe que não é um numero inteiro

"""
numero = input("Digite um numero inteiro: ")

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
else:
    print("Isso não é um numero inteiro")


"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito,
exiba a saudação adequada. Ex:
Bom dia 0-11   
Boa tarde 12-17
Boa noite 18-23
"""
horas = input ("Que horas são? " )

if horas.isdigit():
     horas = int(horas)
     if 0 <= horas <= 11:
         print(f"Bom dia")
     elif 12 <= horas <= 17:
         print(f"Boa tarde")
     elif 18 <= horas <=23:
         print("Boa noite")
     else:
         print(f"Hora inválida")

"""Faça um programa que peça o primeiro nome do usuario. Se o nome tive 4 letras ou menos,
exiba "Seu nome é curto"; se tiver entre 5 e 6 letras, exiba "Seu nome é normal";
maior que 6 letras, exiba "Seu nome é muito grande".
"""

nome = input("Digite seu primeiro nome: ")

tamanho_nome = len(nome)
if tamanho_nome <=4:
    print(f'Seu nome é curto')

elif 5 <= tamanho_nome <=6:
    print(f"Seu nome é normal")

else: 
    print(f'Seu nome é muito grande')