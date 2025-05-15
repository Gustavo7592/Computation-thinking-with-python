# # import pandas as pd
# # import matplotlib.pyplot as plt
# # dados = pd.read_csv('C:/Users/labsfiap/Desktop/Fiap/manutencao_preditiva(in).csv')

# # x = dados['UDI']
# # y1 = dados['Temperatura Ar [K]']
# # y2 = dados['Temperatura Processo [K]']
# # # y3 = dados['Torque [Nm]']

# # plt.plot(x, y1, x, y2)
# # plt.xlabel('Amostras')
# # plt.ylabel('Temperatura')
# # plt.legend('Ar', 'Processo')
# # plt.show()
# # dados.info()


# # dicionario = {
# #     'Pessoas': ['Ana', 'Laura', 'Paulo', 'João'],
# #     'Idade': [19, 25, 45, 34],
# #     'Profissão': ['Contadora', 'Cientista', 'Engenheiro', 'Policial']
# #     }

# # num = int(input("Digite um numero inteiro: "))
# # print(f"Voce digitou o numero: {num}")

# try:
#     num = int(input("Digite um numero inteiro: "))
#     print(f"Voce digitou o numero: {num}")
# except ValueError:
#     print("Isso nao é um numero")
    
# try:
#     a  = int(input("Digite um numero inteiro: "))
#     b  = int(input("Digite um numero inteiro: "))
#     resultado = a/b
#     print(f" O resultado foi: {resultado}")
# except ZeroDivisionError:
#     print("Não é possivel dividir por 0")
# except ValueError:
#     print("Isso não é um numero inteiro")
    
# def entrada_numeros():
#     try:
#         numero = int(input("Digite um numero inteiro: "))
#         print(f" O numero digitado é {numero}")
#     except ValueError:
#         print("Isso nao é um numero")
# entrada_numeros()
# #############################################
# def acesso_lista():
#     lista = [10, 20, 30, 40, 50]
#     try:
#         indice = int(input("Digite um indice para acessar um valor da lista: "))
#         print(f"O valor do indice é {indice} é {lista[indice]}")
        
#     except IndexError:
#         print(f"Insira um indice valido")
#     except ValueError:
#         print("Erro: Insira um numero inteiro")
# acesso_lista()

#############################################

# Ex.1 Crie um algoritmo para converter temperatura celsius em fahreinheit

# Fah = (celsius * 9/5) + 32

# ValueError insira um valor valido

# def conversao():
#     try:
#         celsius = int(input("Digite o valor em celsius: "))
#         fah = (celsius * 9/5) + 32
#         print(f"A temperatura em Fahrenheit é: {fah}")
#     except ValueError:
#         print("Insira um valor valido")
        
# conversao()

# Ex.2 Crie um algoritmo para calcular a area do circulo e do retangulo usando try/except
# função def
# try/except
# estrutura de condição

# area circulo = 3.1415 * raio**2
# retangulo = lado1 * lado2

def area():
    try:
         apresentacao = str(input("Somos uma calculadora de areas (retangulo e circulo) Deseja saber alguma area: "))
         if apresentacao == 'sim':
              raio = int(input("Digite o raio do circulo: "))
              base = int(input("Digite a base do retangulo: "))
              altura = int(input("Digite a altura do retangulo: "))
              retangulo_area = base * altura
              circulo_area = 3.14 * raio**2
              escolha = str(input("Qual area deseja saber? "))
         if escolha == 'circulo':
                  print(f"A area do circulo é {circulo_area}")
         elif escolha == 'retangulo':
                  print(f"A area do retangulo é {retangulo_area}")
                  saber = str(input("Deseja saber a outra area? "))
    except ValueError:
        print("Valor invalido")
area()