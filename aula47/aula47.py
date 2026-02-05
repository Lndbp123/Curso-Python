palavra_chave = 'leonardo'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    if letra_digitada in palavra_chave:
        letras_acertadas += letra_digitada


    palavra_formada = ''
    for letra in palavra_chave:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(f'Palavra formada até agora: {palavra_formada}')
    if palavra_formada == palavra_chave:
        print(f'Parabéns! Você ganhou! A palavra era {palavra_formada}')
        print(f'Fim do jogo.')
        print(f'Número de tentativas: {tentativas}')
   