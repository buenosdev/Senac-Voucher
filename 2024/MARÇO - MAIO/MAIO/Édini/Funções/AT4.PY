# Maior e Menor Número:
# Programe um software que recebe três números e cria duas funções: uma que retorna o 
# maior número e outra que retorna o menor número

def maior(num1,num2):
    if num1 > num2:
        return True  
def func():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    if maior(num1,num2):
          print(f"Numero {num1} é maior que {num2}")
    else:
         (print(f"Numero {num2} é maior que {num1}"))

func()