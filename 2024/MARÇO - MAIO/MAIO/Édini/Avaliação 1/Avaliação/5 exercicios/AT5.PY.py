# 5 - Num país imaginário chamado Lisarb, todas as pessoas ficam muito felizes em pagar os seus
# impostos porque sabem que não existem políticos corruptos e que os impostos são usados para
# beneficiar a população, sem qualquer apropriação indevida. A moeda deste país é o Rombus (R$).
# Leia um valor com 2 dígitos após a vírgula, equivalente ao salário de um habitante do Lisarb. Em
# seguida, imprima o valor devido que essa pessoa deverá pagar de impostos, conforme tabela abaixo:

# Se o salário for de R$ 3.002,00 por exemplo, a alíquota de 8% é sobre R$ 1.000,00, pois o salário
# de R$ 0,00 a R$ 2.000,00 é isento de impostos. No exemplo a seguir, a alíquota total é de 8% sobre
# R$ 1.000,00 + 18% sobre R$ 2,00, resultando em R$ 80,36 ao todo. 
# Entrada:
# A entrada contém apenas um número de ponto flutuante, com 2 dígitos após o ponto decimal.
# Saída:
# Imprima a mensagem “R$” seguida de um espaço em branco e o valor total do imposto a pagar,
# com dois dígitos após a vírgula. Se o valor for até 2000, imprima a mensagem "Isento".
# Exemplo 1:
# Entrada: 3002.00 
# Saída: R$ 80.36
# Exemplo 2:
# Entrada: 1701.12
# Saída: Isento


salario = float(input("Digite o valor do salário: "))

if salario <= 2000:
    imposto = 0
    print("Isento")
elif salario <= 3000:
    imposto = (salario - 2000) * 0.08
elif salario <= 4500:
    imposto = (1000 * 0.08) + ((salario - 3000) * 0.18)
else:
    imposto = (1000 * 0.08) + (1500 * 0.18) + ((salario - 4500) * 0.28)


if imposto > 0:
    print(f"R$ {imposto}")
