"""

Interando strings com while

"""
#        Indices
#        0123456789......................33

frase = 'o rato roeu a roupa do rei de roma'
tannho_frase=len(frase)
controle = 0
nova_string = ''
letraop = input("Qual retra quer substituir?")
"""
while controle < tannho_frase:
    print(frase[controle], controle)
    nova_string += frase[controle]
    print(nova_string)
    controle +=1

print(nova_string)

while controle < tannho_frase:
    letra = frase[controle]
    if letra == letraop:
        nova_string +=letraop.upper()
    else:
        nova_string += letra
    controle +=1
"""

while controle < tannho_frase:
    letra = frase[controle]
    if letra == letraop:
        nova_string += letraop.upper()
    else:
        nova_string += letra
    controle += 1

print(nova_string)