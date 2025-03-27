# # # Exemplo - 1

# # num1 = int(input("Insira um número:"))
# # num2 = int(input("Insira um número:"))
# # dia = input("digite o dia da semana:")

# # if num1 > num2 and dia == "quarta":
# #     print("numero 1 maior e hoje é quarta")
# # elif num1 == num2:
# #     print("os numero sao iguais")
# # else:
# #     print("numero 2 é maior")

# # Exercicio - 2 Crie um programa 

# # velocidade = int(input("insira a velocidade:"))
# # velocidademaxima = 80
# # velocidademinima = 50


# # if velocidade > velocidademaxima:
# #     multa = (velocidade - 80) * 50 
# #     print(f" a sua multa foi de {multa}")

# # #Exercicio - 3
# # elif velocidade < velocidademinima:
# #     multa = (50 - velocidade) * 25
# #     print(f"sua velocidade estava a baixo de {velocidademinima} logo sua multa de foi de {multa}R$")

# # Exercicio - 4 Verifique se um numero é par ou impar usando estrutura de inputa para usuario

# numero = int(input("Digite um numero:"))
    
# if numero %2 == 0:
#     print("Seu numero é par:")
# else:
#     print("Numero é impar:")

# # Exercicio 5

# numero1 = float(input("Digite um numero para calcular"))
# sinal = str(input("digite o sinal"))
# numero2 = float(input("Digite outro numero para calcular"))


# if sinal == "+":
#     resultado = numero1 + numero2
# elif sinal == "*":
#     resultado = numero1 * numero2
# elif sinal == "/":
#      resultado = numero1 / numero2
# elif sinal == "-":
#     resultado = numero1 - numero2
# print(resultado)

#Exercicio - 6 - Crie um programa que solicite dia do mes (1 a 30) e dia da semana (dominga a segunda). Se o dia estiver entre 5 e 10 e o dia da semana nao for domingo ou sabado, mostre que sera dia de pagamento. Se dia estiver entre 5 e 10 e nao for um dia util mostre que o pagamento sera feito em um dia util.

diaMes = int(input("Digite um dia do mes entre 1 e 30"))
diaSemana = str(input("Digite o dia da semana"))

if (diaMes >= 5 or diaMes <= 10) and not (diaSemana != "sabado" or diaSemana != "domingo"):
    print("Sera dia de pagamento")
elif (diaMes >= 5 or diaMes <= 10) and (diaSemana == "sabado" or diaSemana == "domingo"):
    print("O pagamento sera feito no proximo dia util")







# Exercicio - 7 crie um algoritmo para solicitar nome de usuario e senha. No entanto, pense em cono solicitar a senha apenas se o usuario estiver correto. Caso esteja correto, solicite senha. Caso esteja correto, deixe o usuario acessar o sistema

# usuario = str(input("Digite seu usuario"))

# Usuario = "Gustavo"

# if usuario == Usuario:
#     senha = str(input("Usuario certo agora digite sua senha"))
#     print("Senha Certa")
# else:
#     print("Usuario errado tente novamento")
