# -*- coding: utf-8 -*-

# biblioteca RPC do Python
import rpyc


requisicao = rpyc.connect("localhost", 8000)

op = int(input(" 1. IMC\n 2. Calcular uma equação do segundo grau\n 3. Retornar o palíndromo de uma palavra\n Opção: "))

if op == 1:
  print("Digitar numeros decimais com ponto!!!")
  altura = input("Digite a altura: ")
  peso = input("Digite o peso: ")

  print(requisicao.root.exposed_imc(altura,peso))
 
elif op == 2: # elif é igual ao else if
  # soma entre dois valores
  v1 = input(" Digite o valor da variavel A: ")
  v2 = input(" Digite o valor da variavel B: ")
  v3 = input(" Digite o valor da variavel C: ")
 
  print(requisicao.root.exposed_equacao(v1, v2, v3))

elif op == 3: # elif é igual ao else if
# soma entre dois valores
  p1 = input(" Digite a palavra: ")
  print(requisicao.root.exposed_palindromo (p1))