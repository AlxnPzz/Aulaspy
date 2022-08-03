"""
For in em Python
Iterando strings com for
Função range (start=0, stop, step=1)
"""

# Utilizando o laço FOR
"""
texto = input("Digite um texto")
c = 0

while c <len(texto):
    print(texto[c])
    c += 1

# Outra forma de fazer a mesma coisa acima é

for letra in texto:
    print (letra)

- Enumerando as voltas do laço:

for n, letra in enumerate(texto):
    print(n, letra)
"""
# Utilizando a função Range
# Função range (start=0, stop, step=1)
# Para decrementar é só colocar o valor do step negativo e inventer o stop com o start (10,0,-1)

for n in range(0,10,1):
    print(n)

