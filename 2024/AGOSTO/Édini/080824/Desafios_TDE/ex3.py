# Tratamento de Erro em Acesso a Dicionários:

# Acesse um dicionário com uma chave inexistente e trate a exceção KeyError. ​

dicio = {"00":0,"01":1,"02":2,"03":3}

chave = input("Digite um valor para o dicionário: ")   
try: 

    valor = dicio[chave]
    print(f"Valor associado a chave '{chave}': {valor}")
except KeyError:
    print("Erro, a chave não foi encontrada")