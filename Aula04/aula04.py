
# Ex.1 
# for i in range(10):
#    print(nome)

# # Ex.2

# for numero in range(1, 11):
#    print(numero)

# # Ex.3

# for k in range(1, 11, 2):
#    print(k)

# Ex.4

# for k in range(3):
#     nome = input("Digite seu nome:")
#     cpf = int(input("Digite o seu CPF:"))
#     email = input("Digite seu e-mail:")
#     print(cpf)
    
# Ex.5
# entrada = input("Digite uma palavra:")

# for i in entrada:
#     print("Caractere", i)

# Ex.6
# for i in range(1,11):
#     if i == 5:
#         print("Valor encontrado", i)
#     break

# Ex.7 
# for k in range(1,6):
#     if k == 3:
#         continue
#     print("Interação", k)

# Ex.8
# for numero in range(1,5):
#     num = numero ** 2
#     print(num)



# soma_quadrados = 0
# for k in range(1, 6):
#     quadrado = k**2
#     soma_quadrados += quadrado
#     print(soma_quadrados)

# Ex.9
# soma_quadrados = 0
# for k in range(1,5):
#     quadrado = k**2
#     soma_quadrados += quadrado
# media = soma_quadrados / 4
# print(media)

# Ex. 10
# quantidade = int(input("Digite um numero"))
# soma = 0

# for k in range (quantidade):
#     numero = float(input(f"Digite um nimero {k+1}"))
#     soma += numero
#     print(soma)
#     print(numero)

# Ex. 11
# lista1 = ['a','b','c']
# lista2= ['ana', 'paulo','pedro']

# for i in lista2:
#     if i == 'paulo':
#         print(i)
#         break

# Ex.12
# palavra = 'banana'
# alvo = 'a'
# contador = 0

# for letra in palavra:
#     if letra == alvo:
#         contador += 1

# print(f"A letra {alvo} aparece {contador} vezes na palavra")

# Ex.13

# frase = input("Digite uma frase: ")
# letra_alvo = input("Digite a letra alvo: ")
# contador = 0

# for k in frase:
#     if k == letra_alvo:
#         contador += 1
# print(contador)


#### EXERCICIOS #######

# Exercicio - 1 Crie um algoritmo para elevar ao cubo apenas os valores de um range = (2, 12, 2).

# for k in range(2,13,2):
#     quadrado = k**2
#     print(quadrado)

# Exercicio - 2 Crie um algoritmo para solicitar 5 valores da compra de produtos em um supermercado. Em seguida, mostre o valor total a ser pago e a media de valores.
# soma = 0
# for k in range(1,6):
#     produtos = int(input("Qual valor do produto?"))
#     soma += produtos
# media = soma / 5
# print(f" o valor total da compra é de {soma} com uma media de {media}")

# Exercicio - 3 Crie um algoritmo que simule uma tabuada. O usuario deverá escolher o valor a qual será multiplicado por 1 ate 10 e mostre os respectivos valores.
# numero = int(input("Digite um valor"))
# for tabuada in range(1, 11):
#     resultado = numero * tabuada
#     print(resultado)
    
# numero = int(input("Digite um numero"))
# for tabuada in range(1, 10):
#     resultado = numero * tabuada
#     print(resultado)

# Exercicio - 4 Crie uma estrutura para solicitar uma quantidade de valores de temperatura em fahrenheit e transforme em temperatura em graus celsius.
# temp_celsius = 5/9 * (temp_fahrenheit - 32)

# quantidade_temp = int(input("Quantas temperaturas voce quer converter?: "))

# for k in range(quantidade_temp):
#     temp_fahrenheit = float(input("Digite a temperatura em fahreinheit: "))
#     temp_celsius = 5/9 * (temp_fahrenheit - 32)
#     print(f" A respectiva temperatura em graus celsius {temp_celsius:.2f}")
    
# Exercicio - 5 Crie um algoritmo que solicite 3 vezes o nome de usuario, senha. Em seguida,  crie uma estrutura para verificar se o usuario e a senha destes usuarios estao corretas

for k in range(1):
    usuario1 = input("Digite seu usuario: ")
    if usuario1 == 'Fiap':
      senha = input("Usuario Correto, Digite a senha: ")
      
      