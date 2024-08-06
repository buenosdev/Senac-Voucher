# 3 - A média harmônica amortizada é definida como:
# onde N é o número de notas a serem usadas na média, ni é a i-ésima nota, e X é o fator de
# amortização. 

# Implemente um algoritmo em Python que calcule a média de 3 notas de um aluno
# digitadas no teclado, com fator de amortização igual a 4. Em seguida, informe se o aluno passou
# (média >= 5) ou não (média < 5).
# Exemplo de entrada:
# N1: 5.0
# N2: 10.0
# N3: 6.5
# Saída:
# Você passou, sua média é 6.8



num1 = float(input('Escreva a 1º nota: '))

num2 = float(input('Escreva a 2º nota: '))

num3 = float(input('Escreva a 3º nota: '))


media = (3 / ((1 / (num1 + 4)) + (1 / (num2 + 4)) + (1 / (num3 + 4)))) - 4

if (media >=5):

  print('Você passou! Sua média é: ', media)  

else:

  print('Você reprovou :( Sua média é: ',media)