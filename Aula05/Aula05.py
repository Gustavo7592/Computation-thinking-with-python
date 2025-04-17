# Ex.1

# for i in range(5):
#     print(i)
    
# # Ex.2

# lista = [1, 2, 3, 4, 5]

# for k in lista:
#     numero = int(input(f"Digite o {i+1°} numero "))
#     print(k)
#     i += 1
    
# Ex.3 

# lista = [1, 2, 3, 4, 5]

# for k in lista:
#     print(k)

#Ex.4

# lista = [1, 2, 3, 4, 5]

# for k in lista:
#     if k %2 == 0:
# print(k)

#Ex.5

# lista_quantidades = []
# lista_frutas = []

# for i in range(5):
#     quantidades = float(input("Digite a quantidade de frutas: "))
#     frutas = input("Digite as frutas: ")
    
#     lista_quantidades.append(quantidades)
#     lista_frutas.append(frutas)

# print(f" Você tem {lista_quantidades} de {lista_frutas}")

###################################

# Estruturas de repetição com while


#Ex.1
# i = 0
# while i <= 5:
#     print("Contagem", i)
#     i += 1
    
#Ex.2

# contador = 5
# while contador >= 1:
#     print("Contagem", contador)
#     contador -= 1
    
# #Ex.3 - Loop infinito
# while True:
#     print("Loop Infinite")
    
#Ex.4
# senha = ""
# while senha != '1234':
#     senha = input("Digite sua senha")
# print("Acesso liberado")

#Ex.5
# senha_correta = 'python123'
# tentativas = 2
# senha = input("Digite sua senha: ")

# while senha != senha_correta and tentativas > 0:
#     tentativas -= 1
#     senha = input("Digite sua senha: ")

# if senha == senha_correta:
#     print("Acesso liberado")
# else:
#     print("Acesso bloqueado")

#Ex.6
# resultado = 1
# numero = 0

# while numero < 5:
#     numero += 1
#     resultado *= numero
# print(resultado)

# resultado = 1
# numero = 1

# #O que acontece

# resultado = 1 * 2 = 2
# resultado = 2 * 3 = 6
# resultado = 6 * 4 = 24
# resultado = 24 * 5 = 120

# Ex.7
# while True:
#     numero = int(input("Digite um número positivo: "))
#     if numero > 0:
#         break
#     print("Numero aceito", numero)

# Exercicios

# EX - 1 Contar de 10 a 1 e imprimir cada numero

# contador = 10
# while contador >= 1:
#     print("Contagem", contador)
#     contador -= 1

# EX - 2  Criar um programa que aceita numeros entre 1 a 10
# numero = int(input("Digite um numero entre 1 e 10: "))

# while numero < 1 or numero > 10:
#     print("Numero invalido!")
#     numero = int(input("Digite um numro entre 1 e 10: "))
# print("Numero aceito", numero)

# EX - 3 Solicitar senhas até que o usuario digite a senha correta.

# senha_correta = '1234'
# senha = input("Digite a senha: ")
# while senha != senha_correta:
#     print("Senha incorreta!")
#     senha = input("Digite a senha: ")
# print("Senha correta!")

# EX - 4 Criar um programa que soma todos os numeros digitados ate que o usuario digite o 0

# numero = int(input("Digite um numero: "))
# soma = 0
# while numero != 0:
#     soma += numero
#     print(f"A soma é {soma}")
#     numero = int(input("Digite um numero: "))
# print(f"A soma final dos números foi {soma}")

# EX - 5 Transformar temperatura fahrenheit para grau Celsius. Enquanto 
# temperatura Fahrenheit for diferente de 0, tranforma em Celsis
# F = ()
# while F != 0:
#     F = float(input("Digite a temperatura em FAHRENHEIT: "))
#     if F == 0:
#         print("Nao posso tranformar")
#         break
#     C = 5/9 * (F - 32)
#     print(C)

    
    

