nome = str(input("Digite o nome do candidado: "))
idade = int(input("Digite a idade do candidato: "))
email = str(input("Digite o e-mail do candidato: "))
cargo = str(input("Digite o cargo que gostaria de adquirir: "))

if idade >= 18:

    print("\nParabéns você passou para a próxima fase!!")
    print(f"Enviaremos novas instruções para seu email: {email}")
else:

    print("\nAgradecemos por sua participação. Infelizmente você não passou para a fase final.")

    exit()

curso = int(input("\nO candidato possui cursos da área? (Digite 1 para SIM, ou, Digite 2 para NÃO): "))

if curso == 1:

    print("\nParabéns você passou para a próxima fase!!")
    print(f"Enviaremos novas instruções para seu email: {email}")
else:

    print("\nAgradecemos por sua participação. Infelizmente você não passou para a fase final.")

    exit()

nota = float(input("\nDigite a nota do candidado na fase 3: "))

if nota >= 7.0:

    print(f"\nParabéns, você passou para a fase final!! Você está bem próximo da sua vaga para {cargo}")
    print(f"Enviaremos novas instruções para seu email: {email}")
else:
    print("\nAgradecemos por sua participação. Infelizmente você não passou para a fase final.")

    exit()

