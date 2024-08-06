
# Gerenciador de Estoque de Supermercado:
# Você é o gerente de um supermercado e precisa criar um sistema
# para gerenciar o estoque de produtos. 
# Desenvolva um programa em python utilizando listas 
# que permita adicionar, remover e exibir os produtos 
# em estoque.
 
#----------Gerenciamento super foda de mercado----------#

# cadastro = []

# while True:
    
#     print("\n--------Menu Legal--------\n")
#     print("Digite 1 para cadastrar um produto")
#     print("Digite 2 para remover um produto")
#     print("Digite 3 para exibir os produtos")
#     print("Digite 0 para sair")
#     print("\n--------------------------\n")    
#     opcao = int(input("\nDigite aqui: "))


#     if opcao == 1:
#         ID = int(input("Digite um ID para o produto: "))
#         nome = str(input("Digite o nome do produto: "))
#         quantidade = int(input("Digite a quantidade desse produto: "))
#         preco =  float(input("Digite o preço do produto: "))

#         cliente =  {"ID": ID,
#                     "nome":nome,
#                     "quantidade":quantidade,
#                     "preco":preco}
    
#         cadastro.append(cliente)

#         print("Produto cadastrado com sucesso.")

#     elif opcao == 2:
#         print("\n--------Menu Legal 2--------\n")
#         print("Qual produto vc deseja remover?")
#         print(f'ID: {ID}, Nome: {nome}, Preço: R${preco}, Quantidade: {quantidade}')
#         print("\n----------------------------\n")    
#         menu = cadastro.pop = (int(input("\nDigite aqui (0 para 1): ")))  

#     elif opcao == 3:
#         print("\nProdutos cadastrados: ")
#         for cliente in cadastro:
#             print(f'Nome: {nome}, Preço: R${preco}, Quantidade: {quantidade}')
    

#     elif opcao == 0:
#         break
#     else:
#         continue




#----------Joguinho super foda de Quiz----------#


# Crie um jogo de quiz com perguntas e respostas, 
# onde o jogador acumula pontos ao acertar as respostas.
# Exemplo de Saída:
# Qual é a capital do Brasil?
# Sua resposta: Br
# Resposta incorreta.
# Quem escreveu 'Dom Quixote'?
# Sua resposta: n sei
# Resposta incorreta.
# Quanto é 2 + 2?
# Sua resposta: 4
# Resposta correta!
# Você fez 1 pontos.

cont1 = 0
cont2 = 0
correto = []
incorreto = []

p1 = input("Qual a capital do Brasil?: ").upper()
p2 = input("Quem escreveu Dom Quixote?: ").upper()
p3 = int(input("Quanto é 2+2?: "))

if p1 == "BRASILIA":
    cont1 += 1

if p2 == "MIGUEL DE CERVANTES":
    cont1 += 1


if p3 == 4:
    cont1 += 1

print(f"Você acertou: {cont1}")


#----------Esse trem aqui----------#

# O engenheiro de uma empresa precisa calcular a quantidade de cabos de rede necessários para instalar um laboratório com "n" pontos de redes. O engenheiro sabe que a distância entre cada ponto de rede será de "r" metros (razão) e que o comprimento total dos cabos é igual à soma das distâncias entre todos os pontos de rede.
# Para facilitar o cálculo, o engenheiro decidiu usar uma Progressão Aritmética (PA) para representar as distâncias entre os pontos de rede. Você precisa escrever um programa Python que ajude o engenheiro a calcular a quantidade de cabos de rede necessários. Seu programa deve:
# Solicitar ao usuário os dados de entrada da PA que é dado por: a + (n-1)*r, onde "a" é o primeiro termo, "n" é o número de termos e "r" é a razão da progressão.
# Calcular total dos cabos de rede necessário, que é igual à soma dos termos de todos os pontos de rede. Exibir na tela a quantidade de cabos de rede necessários para instalar o laboratório.
# Exibir também quarto termo e o termo central da progressão aritmética.
# Para calcular o termo central o programa deve somar o 1º e ultimo termo da Progressão Aritmética e dividir por 2.
# Por fim, o programa deve retornar uma lista com os termos da PA e ser testado com diferentes valores de "n" e "r" para garantir que ele esteja funcionando corretamente e produzindo resultados precisos.
# Entrada


# >>Digite o primeiro termo da PA: 2
# >>Digite a razão: 1.5
# >>Digite a quantidade de termos: 7
 
 
# Saída


# >> [2.0, 3.5, 5.0, 6.5, 8.0, 9.5, 11.0]
# >> O quinto termo é: 8.0
# >> O termo central é: 6.5
# >> Soma dos termos: 45.5
 
# Entrada


# >>Digite o primeiro termo da PA: 3
# >>Digite a razão: 2.5
# >>Digite a quantidade de termos: 7
 
 
# Saída


# >> [3.0, 5.5, 8.0, 10.5, 13.0, 15.5, 18.0]
# >> O quinto termo é: 13.0
# >> O termo central é: 10.5
# >> Soma dos termos: 73.5
# Obs. Não é permitido a utilização bibliotecas
# Obs. Utilizar tratamento de exceção



    
    


 

 