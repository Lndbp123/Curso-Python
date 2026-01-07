#Operadores logicos
#and (e)
#or (ou)    
#not (não)

#verdadeiras.
#Se qualquer valor for considerado verdadeiro, o resultado será verdadeiro.
#Se todos os valores forem considerados falsos, o resultado será falso.

entrada = input('[E]ntrar ou [S]air: ')
senha_usuario = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_usuario == senha_permitida:
    print("Você entrou no sistema!")

elif (entrada == 'E' or entrada == 'e') and senha_usuario != senha_permitida:
    print("Senha incorreta. Tente novamente.")

elif entrada == 'S' or entrada == 's':
    print("Você saiu do sistema!")

