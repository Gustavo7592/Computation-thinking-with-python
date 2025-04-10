#  EX.1 - Estrutura de entrada e saida

# var_1 = int(input("Digite um numero inteiro: "))
# var_2 = float(input("Digite um numero nao inteiro: "))
# var_3 = str(input("Digite uma palavra: "))

# print(f"O numero inteiro é {var_1}")
# print(f"O numero nao inteiro é {var_2:.03f}")
# print(f"A palavra é {var_3}")

########################################

# Ex.2

# nome = str(input("Digite seu nome: "))

# if nome == 'fiap':
#     rgm = int(input("Digite seu RGM: "))
#     if rgm == 1234:
#         print("Acesso permitido")
#     else:
#         print("RGM esta incorreto")
#         rgm = int(input("Digite seu RGM: "))
#         if rgm == 1234:
#             print("Acesso permitido")
#         else:
#             print("Seu RGM esta incorreto e voce foi bloqueado")

# else:
#     print("Nome incorreto")

##########################################

# Ex.3

# nome = str(input("Digite seu nome: "))
# rgm = int(input("Digite seu RGM: "))
# if nome == 'fiap' or rgm == 1234:
#     print('Acesso permitido')
# else: 
#     print('acesso negado!')

# Ex.4
 
# Crie um algoritmo para calcular a area e o perimetro em função das formas
 # geometricas (quadrado, circulo e triangulo).

# area das formas geometricas

# quadrado = lado1 * lado2
# retangulo = lado1 * lado2
# circulo = pi* raio * raio
# triangulo = (base * altura) / 2

# Perimetro das formas geometricas

# quadrado = (lado1*2) + (lado2*2)
# retangulo = (lado1*2) + (lado2*2)
# circulo = 2pi * raio
# triangulo = base * altura + hipotenusa

# from math import pi

# formaGeometrica = str(input("Digite uma forma geometrica: quadrado,retangulo, circulo ou triangulo: "))
# if formaGeometrica == 'quadrado' or formaGeometrica == 'retangulo' :
#     lado1 = float(input("Digite o lado 1: "))
#     lado2 = float(input("Digite o lado 2: "))
#     resultado = lado1 * lado2
#     resultadoP = (lado1*2) + (lado2*2)
#     print(f'O seu perimetro é de {resultadoP} e a area é de {resultado}')
# elif formaGeometrica == 'circulo':
#    raio = float(input(f"Digite o raio do circulo: "))
#    circulo = pi* raio * raio
#    circuloP = 2*pi * raio
#    print(f'a area do seu circulo é {circulo:.02f} e o perimetro é de {circuloP:.02f}')
   
# elif formaGeometrica ==  'triangulo':
#     base = float(input("Digitie a base: "))
#     altura = float(input("Digite a altura: "))
#     hipotenusa = float(input("Digite a hipotenusa "))
#     trianguloA = (base * altura)/lado2
#     trianguloP = base * altura + hipotenusa

# numero_1 = int(input("Digite o primeiro número: "))
# numero_2 = int(input("Digite o segundo numero: "))
# numero_3 = int(input("Digite o terceiro numero: "))

# if numero_1 > numero_2 and numero_1 > numero_3:
#     print(f"O maior numero é {numero_1}")
# elif numero_2 > numero_1 and numero_2 > numero_3:
#     print(f'O maior numero é o {numero_2}')
# elif numero_3 > numero_1 and numero_3 > numero_2:
#     print(f'O maior numero é o {numero_3}')
# if numero_1 == numero_2 or numero_1 == numero_3 or numero_2 == numero_3:
#     print(f"Existem valores iguais: {numero_1}, {numero_2}, {numero_3}")

# # Exercicio - 2 Crie um programa 

# consumo = float(input("insira o consumo de energia em kWh:"))
# if consumo <= 50:
#      conta = consumo * 0.50
#      print(f'a sua conta nao ultrapassou 50kWh e teve o valor de {conta} R$')
# elif consumo <= 100:
#     conta = consumo * 0.75 
#     print(f' A sua conta ficou entre 51kWh e 100kWh teve o valor de {conta} R$')
# else:
#     conta = (consumo * 1.20) + 5
#     print(f' A sua conta ultrapassou 100kWH e teve o valor de {conta:.02f} R$')

# turbina = str(input("Digite o tipo de turbina: "))
# vazao = str(input("Qual foi a vazão de agua: "))

# if turbina == 'kaplan' and vazao == 'alta' or turbina == 'pelton' and vazao == 'baixavazão':
#     print("Eficiencia Maxima")
# elif turbina == 'francis' and vazao != 'baixa':
#     print('Eficiencia moderada!')
# else:
#     print('Eficiencia Minima')

# usuarios = ["admin", "tomas", "gustavo"]
# senhas = ["12345", "tomas123", "gustavo123"]
# nome_usu = input("Digite o nome de usuário: ")
# if nome_usu == "admin":
#     senha = input("Digite a senha: ")
#     if senha == "12345":
#         print("Acesso concedido")
#     else:
#         print("Senha incorreta")
# elif nome_usu in usuarios:
#     index = usuarios.index(nome_usu)  
#     print("Acesso limitado")    
# else:
#     print("Usuário não reconhecido")
    
# numero_1 = int(input("Digite o primeiro número: "))
# numero_2 = int(input("Digite o segundo numero: "))
# numero_3 = int(input("Digite o terceiro numero: "))

# if numero_1 > numero_2 and numero_1 > numero_3:
#     print(f"O maior numero é {numero_1}")
# elif numero_2 > numero_1 and numero_2 > numero_3:
#     print(f'O maior numero é o {numero_2}')
# elif numero_3 > numero_1 and numero_3 > numero_2:
#     print(f'O maior numero é o {numero_3}')
# if numero_1 == numero_2 or numero_1 == numero_3 or numero_2 == numero_3:
#     print(f"Existem valores iguais: {numero_1}, {numero_2}, {numero_3}")
 
# consumo = float(input("insira o consumo de energia em kWh:"))
# if consumo <= 50:
#      conta = consumo * 0.50
#      print(f'a sua conta nao ultrapassou 50kWh e teve o valor de {conta} R$')
# elif consumo <= 100:
#     conta = consumo * 0.75 
#     print(f' A sua conta ficou entre 51kWh e 100kWh teve o valor de {conta} R$')
# else:
#     conta = (consumo * 1.20) + 5
#     print(f' A sua conta ultrapassou 100kWH e teve o valor de {conta:.02f} R$')

    
    
    
       
   
    
    
    
    
    



    