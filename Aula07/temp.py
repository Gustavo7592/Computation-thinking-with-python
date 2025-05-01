# # Exemplo para transformar temperatura em fahnreiheit em graus celsius:
    
# temp_celsius = 0
# lista_temp_celsius = []


# temp_fahr = float(input("Digite a temperatura em fahreiheit: "))

# while temp_fahr != 0:
#     temp_celsius = 5/9 * (temp_fahr - 32)
#     temp_fahr = float(input("Digite a temperatura em fahreiheit: "))
#     lista_temp_celsius.append(temp_celsius)
#     print(lista_temp_celsius)
    
# soma_temp_celsius = 0
# media_temp_celsius = 0
# taxa_temp_celsius = 0

# for temp in lista_temp_celsius:
#     soma_temp_celsius += temp

# media_temp_celsius = soma_temp_celsius / len(lista_temp_celsius) 
# taxa_temp_celsius = lista_temp_celsius / media_temp_celsius  
# print(f"A soma é {soma_temp_celsius}")
# print(f"A media é {media_temp_celsius}")
# print(len(lista_temp_celsius))
# print(taxa_temp_celsius)
#     # temp += 1

# lista_frutas = ['maça', 'laranja', 'banana', 'kiwi']

# for i in range(len(lista_frutas)):
    # print(f"Fruta {i}: {lista_frutas[i]}")
    
# print(len(lista_frutas))

# 6.Crie um algoritmo que permita ao usuário criar uma lista de tarefas com prioridade.
# Permita que o usuário adicione 8 tarefas com suas respectivas prioridades (por exemplo: "Estudar Python - Alta")
# . Armazene cada tarefa como uma string em uma lista vazia. Use uma estrutura de repetição for ou while 
# para a entrada de dados e, ao final, retorne a lista de tarefas ordenada por prioridade (Alta, Média, Baixa).
# lista_tarefas = []
# lista_prioridade = []
# lista_alta = []
# lista_media = []
# lista_baixa = []

# for i in range(4):
#         lista_tarefas.append(str(input("Digite suas tarefas: ")))
#         lista_prioridade.append(str(input("Digite sua prioridade: ")))
        
        
# for prioridade in lista_prioridade:
#     if prioridade == 'alta':
#         lista_alta.append(prioridade)
#     elif prioridade == 'media':
#         lista_media.append(prioridade)
#     else:
#         lista_baixa.append(prioridade)
        
# print(lista_alta)
# print(lista_media)
# print(lista_baixa)

Criei 5 listas sendo as duas primeiras para pedir uma informação de tarefas e prioridade, seguindo das listas para guardar e organizar as prioridades (alta, media e baixa) apos isso usei FOR em um range de 8 para repetir a captação da informação 8 vezes por meio input e guardei essas informações dentro listas tarefas e prioridades que estavam vazias, apliquei outro FOR para a setar o loop de organização por meio de uma estrutura de condição IF assim conseguindo a organização das prioridades (alta em primeiro, media em segundo, baixa em terceiro) nas condições de ALTA, MEDIA E BAIXA, para saber o resultado printei as listas (lista_alta, lista_media e lista_baixa)

#Criei 5 listas sendo as duas primeiras para pedir uma informação (tarefa e prioridade), seguindo das listas de prioridades (alta, media e baixa) apos isso usei for em um range de 8 para pedir 8 vezes     
