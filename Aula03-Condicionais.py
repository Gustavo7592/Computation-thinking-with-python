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

numero = int(input("Digite um numero:"))
    
if numero %2 == 0:
    print("Seu numero é par:")
else:
    print("Numero é impar:")

# Exercicio 5

numero1 = float(input("Digite um numero para calcular"))
sinal = str(input("digite o sinal"))
numero2 = float(input("Digite outro numero para calcular"))


if sinal == "+":
    resultado = numero1 + numero2
elif sinal == "*":
    resultado = numero1 * numero2
elif sinal == "/":
     resultado = numero1 / numero2
elif sinal == "-":
    resultado = numero1 - numero2
print(resultado)
