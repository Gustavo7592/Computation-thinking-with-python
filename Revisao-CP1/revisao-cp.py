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

from math import pi

formaGeometrica = str(input("Digite uma forma geometrica: quadrado,retangulo, circulo ou triangulo: "))
if formaGeometrica == 'quadrado' or formaGeometrica == 'retangulo' :
    lado1 = float(input("Digite o lado 1: "))
    lado2 = float(input("Digite o lado 2: "))
    resultado = lado1 * lado2
    resultadoP = (lado1*2) + (lado2*2)
    print(f'O seu perimetro é de {resultadoP} e a area é de {resultado}')
elif formaGeometrica == 'circulo':
   raio = float(input(f"Digite o raio do circulo: "))
   circulo = pi* raio * raio
   circuloP = 2*pi * raio
   print(f'a area do seu circulo é {circulo:.02f} e o perimetro é de {circuloP:.02f}')
   
elif formaGeometrica ==  'triangulo':
    base = float(input("Digitie a base: "))
    altura = float(input("Digite a altura: "))
    hipotenusa = float(input("Digite a hipotenusa "))
    trianguloA = (base * altura)/lado2
    trianguloP = base * altura + hipotenusa
    
    
    
       
   
    
    
    
    
    



    