"""
Entrada de dados - Input
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nascimento = 2022-int(idade) #aqui eu transformei a idade de str para inteiro
print(f'Olá {nome} sua idade é {idade} anos. '
      f'Você nasceu em {ano_nascimento}')


#Calculadora
numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite um numero: '))
calc = numero_1+numero_2
print(f'A soma de {numero_1} mais {numero_2} é de {calc}')