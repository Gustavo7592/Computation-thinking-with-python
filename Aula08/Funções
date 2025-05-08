# Aula 08 - Função


# def funcao(parametro1, parametro2):
#     total = parametro1 * parametro2
#     return total, ... , ...


# def eleva_quadrado(x):
#     quadrado = x * x
#     return quadrado
# eleva_quadrado(10)

# def segundo_grau(x):
#     resultado = eleva_quadrado(x) + 10 * x + 5
#     return resultado

## Exemplo 1

# def saudacao():
#     print("Olá!")
# saudacao()

# # Exemplo 2

# def saudacao_personalizada(nome):
#     print(f"Olá {nome}. Seja bem vindo!")
# saudacao_personalizada("Gustavo")

# Exemplo 3
# def saudacao_personalizada(nome):
#     print(f"Olá {nome}. Seja bem vindo!")
    
# name = str(input("Insira seu nome: "))
# saudacao_personalizada(name)

# Exemplo 4

# def media(a, b):
#     resultado_media = (a + b) / 2
#     return resultado_media
# x = float(input("Digite um número: "))
# y = float(input("Digite um número: "))

# print(media(x, y))

# Exemplo 5

# def medias(a, b, c, d):
#     result_media1 = (a + b) / 2
#     result_media2 = (c + d) / 2
#     return result_media1, result_media2

# x, y = medias(10, 5, 3, 2)
# print(x)
# print(y)

##########################################

# Exercicios

#  1. Crie um algoritmo para calcular o resultado de uma equação do primeiro grau 10x + 5 utilizando função

# def equacao(x):
#     resultado = (10 * x) + 5
#     return resultado
# a = float(input("Digite o valor de x: "))
# print(equacao(a))

# 2. Crie uma função para calcular a área de um retângulo e quadrado em uma unica função
# def area(a, b):
#     result_area1 = a * b 
#     result_area2 = a ** 2
#     return result_area1, result_area2
# x = float(input("Digite o valor da base: "))
# y = float(input("Digite o valor da altura: "))
# print(area(x, y))

 
# 3. Crie uma função a qual seja possível calcular o resultado de uma equação do segundo, apartir de duas equaçoes de 
# primeiro grau.

# def equacao(a1, a2, b1, b2):
#     A = a1 * a2
#     B = (a1 * b2) + (a2 * b1)
#     C = b1 * b2
#     x1 = (-B + (B**2 - 4 * A * C) **0.5) / 2*A
#     x2 = (-B - (B**2 - 4 * A * C) **0.5) / 2*A
#     return x1, x2
# print(equacao(-1, -2, 3, 2))
# X1, X2 = equacao(-1, -2, 3, 2)
# print(X1)
# print(X2)

# def eleva_quadrado(x):
#     quadrado = x*x
#     return quadrado

# def equacao_segundo_grau(x):
#     resultado = eleva_quadrado(x) + (10*x) - 5
#     return resultado
# equacao_segundo_grau(5)

############################################

# calcular media

# Exemplo 1

# def calcula_media(lista):
#     soma = 0
#     for i in lista:
#         soma += i
#     media = soma /len(lista)
    
    
#     return media

# Exemplo 2

# def calculo_media(lista):
#     return sum(lista) / len(lista)

# lista_numeros = [10, 20, 30, 40, 50]
# print(calculo_media(lista_numeros))

# # Exemplo 3
# def maior_valor(lista):
#     valor_max = max(lista)
#     return valor_max

# lista_numeros = [10, 20, 30, 40, 50]
# print(maior_valor(lista_numeros))

# Exercicios 
 
# Exercicio 1 Crie um função para calcular a soma de números de uma lista. crie uma função que calcule a 
# media usando a função que calcule a soma

lista_numeros = [100, 200, 300, 400, 500]

def soma_lista(lista): 
    soma = 0
    for i in lista:
        soma += i
    return soma

def media_lista(lista):
    media = soma_lista(lista_numeros) / len(lista)
    return media
print(media_lista(lista_numeros))