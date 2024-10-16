# Lista de Exercícios (10/10)
# 1 - Crie uma função que calcule o fatorial de um número dado pelo usuário.
# 2 - Desenvolva um programa que mostre a tabuada de um número informado pelo usuário.
# 3 - Escreva uma função que verifique se uma palavra ou frase é um palíndromo (pode ser lida da mesma maneira de trás para frente).
# 4 - Faça um programa que verifique se um número fornecido é primo.
# 5  - Desenvolva uma função que mostre os n primeiros termos da sequência de Fibonacci, onde n é informado pelo usuário.
# 6 - Escreva um algoritmo que receba uma lista de números e retorne a lista ordenada de forma crescente (Bubble sort).
# 7 - Faça um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa. O usuário deverá escolher a conversão desejada.
# 8 - Crie um algoritmo que receba 5 números e exiba o maior e o menor número informados.


# 1 - Função que calcula o fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

# 2 - Programa que mostra a tabuada de um número informado
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# 3 - Função que verifica se uma palavra ou frase é um palíndromo
def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

# 4 - Função que verifica se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 5 - Função que mostra os n primeiros termos da sequência de Fibonacci
def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

# 6 - Função que ordena uma lista de números usando Bubble Sort
def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# 7 - Funções que convertem temperaturas de Celsius para Fahrenheit e vice-versa
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

# 8 - Função que recebe uma lista de números e retorna o maior e o menor
def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

# Programa principal que usa todas as funções criadas

# Fatorial
num = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {num} é {fatorial(num)}")

# Tabuada
num = int(input("\nDigite um número para mostrar a tabuada: "))
tabuada(num)

# Palíndromo
frase = input("\nDigite uma palavra ou frase para verificar se é um palíndromo: ")
if eh_palindromo(frase):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

# Número primo
num = int(input("\nDigite um número para verificar se é primo: "))
if eh_primo(num):
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")

# Sequência de Fibonacci
n = int(input("\nQuantos termos da sequência de Fibonacci deseja mostrar? "))
print(f"Os {n} primeiros termos da sequência de Fibonacci são: {fibonacci(n)}")

# Bubble Sort
numeros = list(map(int, input("\nDigite uma lista de números separados por espaço para ordená-los: ").split()))
print(f"Lista ordenada: {bubble_sort(numeros)}")

# Conversão de temperaturas
opcao = input("\nDigite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: ").upper()
if opcao == 'C':
    c = float(input("Digite a temperatura em Celsius: "))
    print(f"{c}°C equivale a {celsius_para_fahrenheit(c):.2f}°F")
elif opcao == 'F':
    f = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"{f}°F equivale a {fahrenheit_para_celsius(f):.2f}°C")
else:
    print("Opção inválida!")

# Maior e menor número
numeros = [int(input(f"\nDigite o {i+1}º número: ")) for i in range(5)]
maior, menor = maior_menor(numeros)
print(f"O maior número é {maior} e o menor número é {menor}.")
