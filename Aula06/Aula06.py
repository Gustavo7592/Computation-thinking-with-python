# # Estruturas com lista

# lista_nomes = ['ana', 'laura', 'pedro', 'melissa']
# lista_cep = [111, 222, 333, 444, 555]
# print(lista_nomes)
# print(lista_cep)

# #######################################

# # Estrutura com dicionario

# dicionario = {
#     'nome': ['ana','laura','pedro','melissa'],
#     'cep': [111, 222, 333, 444]
# }
# print(dicionario)

# import pandas as panda
# dataframe = panda.DataFrame(dicionario)
# dataframe

# Ex.1
# lista_frutas = []
# for k in range(5):
#     frutas = input("Digite sua fruta favorita: ")
#     lista_frutas.append(frutas)
# print(lista_frutas)

# for i in lista_frutas:
#     if i == 'maça':
#         print(i)
#         break
# print(i)   


# lista_frutas = ['maça', 'banana', 'laranja']

# for k in lista_frutas:
#     print(k)
    
# lista_numeros = [10, 20, 30, 40, 50]

# for k in lista_numeros:
#     print(k)

##########################
# lista_nome = []
# lista_cpf = []

# for k in range(5):
#     nomes = input("Digite sue nome: ")
#     cpf = int(input("Digite seu cpf: "))
#     lista_nome.append(nomes)
#     lista_cpf.append(cpf)
# print(lista_nome)
# print(lista_cpf)
# #############################

# lista_frutas = ['maça', 'laranja', 'banana', 'kiwi']

# for i in range(len(lista_frutas)):
    # print(f"Fruta {i}: {lista_frutas[i]}")
    
# print(len(lista_frutas))

#############################

# texto = 'python'
# for letra in texto:
#     print(letra)
    
###############################

# numeros = [2, 4, 6, 8] # ---> 0 + 2 = 2 + 4 = 6 + 6 = 12 + 8 = 20
# soma = 0

# for k in numeros:
#     soma += k
# print(soma)

# ############################
# numeros = [2, 4, 6, 8] 

# for numero in numeros:
#     quadrado = numero**2
#     print(f"O quadrado de {numero} é {quadrado}")

#########################

# palavras = ['casa', 'computador', 'sol', 'programação']
# lista_palavras = []
# for k in palavras:
#     if len(k) > 3:
#         print('palavra maior')
#         lista_palavras.append(k)
#         print(lista_palavras)
# #########################
# Crie um algoritmo para somar apenas os numeros pares da lista

# lista = [1, 6, 7, 10, 13, 16]
# lista_numeros = 0

# for k in lista:
#     if k % 2 == 0:
#         lista_numeros += k
# print(lista_numeros)

############################

# lista_a = [1, 6, 7, 10, 13, 16]
# lista_b = [6, 13, 10, 7, 4, 1]
# lista_c = ['a', 'b', 'c', 'e', 'f']

# lista_nova = []

# lista_nova.append([lista_a, lista_b, lista_c])
# print(lista_nova)
# print(lista_nova[0][1])  

# Estruturas de repetição aninhada

for i in tange(1,4):
    for k in range(1,4):
        print(f'{i}x{k} = {i*k}')