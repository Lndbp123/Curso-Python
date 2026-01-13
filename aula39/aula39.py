nome = "LEONARDO"
tamanho_nome = len(nome)

nova_formula = ''  # Começa com string VAZIA, não com 0
indice = 0

while indice < tamanho_nome:
    nova_formula += f'*{nome[indice]}'  # Adiciona * e a letra
    indice += 1

nova_formula += '*'  # Adiciona o último * no final
print(nova_formula)  # Resultado: *L*E*O*N*A*R*D*O*