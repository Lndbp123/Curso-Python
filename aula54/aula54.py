"""
Faça uma lista de compra com listas
O usuario deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

lista_de_compras = []

while True:
    print("Selecione uma opção:")
    opcao = input("[i]nserir [a]pagar [l]istar [s]air: ")
    if opcao == 'i':
        item = input("Digite o item para adicionar na lista de compras: ")
        lista_de_compras.append(item)
    elif opcao == 'a':
        indice_str = input("Digite o índice do item que deseja apagar: ")
        if not indice_str.isdigit():
            print("Por favor, digite um número válido.")
            continue
        indice = int(indice_str)
        if 0 <= indice < len(lista_de_compras):
            del lista_de_compras[indice]
            print(f"Item no índice {indice} removido.")
        else:
            print("Índice inválido. Tente novamente.")
    elif opcao == 'l':
        if not lista_de_compras:
            print("A lista de compras está vazia.")
        else:
            for i, item in enumerate(lista_de_compras):
                print(f"{i}: {item}")
    elif opcao == 's':
        print("Saindo da aplicação.")
        break
    else:
        print("Opção inválida. Tente novamente.")


   

  