lista_par = []
contador = 1
while contador < 11:

    num = int(input(f"Digite o {contador}º numero: "))

    if num%2 == 0 :
        lista_par.append(num)

    contador += 1 

print(lista_par)
print(f"A soma dos números pares é: {sum(lista_par)}")


