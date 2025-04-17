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

