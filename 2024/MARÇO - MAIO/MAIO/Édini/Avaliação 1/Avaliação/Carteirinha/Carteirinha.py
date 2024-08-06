nome1 = input("Digite o nome da pessoa: ")
valor1 = float(input("Digite o valor do ingresso: "))
tipo1 = input("Digite o tipo do ingresso (inteira ou meia): ")

if tipo1 == 'meia' or tipo1 == 'Meia' or tipo1 == 'MEIA':
    carteirinha1 = input("Digite o número da carteirinha de estudante: ")
    if not carteirinha1:
        print("Você precisa apresentar uma carteirinha de estudante para comprar ingresso meia.")
        exit() 

nome2 = input("Digite o nome da segunda pessoa: ")
valor2 = float(input("Digite o valor do ingresso: "))
tipo2 = input("Digite o tipo do ingresso (inteira ou meia): ")

if tipo2 == 'meia' or tipo2 == 'Meia' or tipo2 == 'MEIA':
    carteirinha2 = input("Digite o número da carteirinha de estudante: ")
    if not carteirinha2:
        print("Você precisa apresentar uma carteirinha de estudante para comprar ingresso meia.")
        exit()  

if tipo1 == 'meia' or tipo1 == 'Meia' or tipo1 == 'MEIA':
    valor1 = valor1 / 2

if tipo2 == 'meia' or tipo2 == 'Meia' or tipo2 == 'MEIA':
    valor2 = valor2 / 2

valor_total = valor1 + valor2


print("\nResumo da compra:")
print(f"Nome:{nome1} \nTipo: {tipo1} \nValor: R$: {valor1}")
print(f"Nome:{nome2} \nTipo: {tipo2} \nValor: R$: {valor2}")
print(f"\nTotal da compra: R$ {valor_total}\n")
