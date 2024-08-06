salario = int(input("Digite o salario do funcionario: "))

if salario < 500:

    print(f"Seu salario foi reajustado para  {(salario * 0.15) + salario}")

elif salario >= 500 and salario <= 1000:
    print(f"Seu salario foi reajustado para  {(salario * 0.10) + salario}")

elif salario > 1000:
    print(f"Seu salario foi reajustado para {(salario * 0.5) + salario}")
