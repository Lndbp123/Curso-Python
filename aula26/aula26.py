"""
Formatação de strings em Python utilizando o método format().
s - string
d e i - int
f - float
<numero de digitos> f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
Ex : 0>-100,.1f
conversion flags - !r !s !a


"""

variavel = "Leonardo"
print(f'Olá, {variavel:s}! Seja bem-vindo(a)!')
print(f'Olá, {variavel!r}! Seja bem-vindo(a)!')
print(f'Olá, {variavel!a}! Seja bem-vindo(a)!')
print(f'Olá, {variavel:^20s}! Seja bem-vindo(a)!')
print(f'Olá, {variavel:>20s}! Seja bem-vindo(a)!')
print(f'Olá, {variavel:<20s}! Seja bem-vindo(a)!')