# Desafio: 

# /--------------Parte 1: 
# Crie um algoritmo de supermercado, onde dentro desse sistema o 
# cliente deve poder adicionar os produtos que quiser separados por seção 
# (vide exemplos na parte 3 do exercício), que aparecem descritas para 
# ele no momento que ele entra no sistema, dentro de cada seção ele faz 
# as escolhas de subtipos e por fim escolhe os produto que vai colocar 
# dentro do carrinho de compras e, se mudar de ideia, pode retirá-los 
# depois, quando o cliente estiver pronto para finalizar a sua compra ele 
# deve ter a opção de finaliza-la e mostrar o valor total de todos os 
# produtos que estiverem no carrinho com o descritivo de quanto custa 
# cada produto e quais são os produtos adicionados. Depois de conseguir 
# visualizar essas informações o cliente deve selecionar uma forma de 
# pagamento (dinheiro, pix, se for cartão deve perguntar qual tipo de 
# cartão: débito, crédito, voucher) caso a forma escolhida seja dinheiro, o 
# sistema deve perguntar quanto está sendo entregue, se o valor for maior 
# deve calcular o troco, se for menor não autorizar a compra e solicitar 
# uma nova forma de pagamento, se for equivalente ao valor total permitir 
# que o cliente pague e leve as compras. Caso ele selecione uma das 
# opções de cartão ou pix, ele deve informar qual o saldo existente, se for 
# maior ou igual o valor da compra, ela é aprovada e o cliente pode 
# finalizar, se for menor, ele não autoriza a compra e deve solicitar uma 
# nova forma de pagamento. 

#  /--------------Parte 2: 
# Deve haver uma validação se o usuário é um funcionário do mercado 
# ou não, se ele for um funcionário, ele deve ter uma matrícula, um nome, 
# uma data de nascimento e um cpf, se ele for um cliente, ele só deverá 
# informar o cpf e o nome. 

#  /--------------Parte 3: 
# Quando o usuário é um funcionário o sistema deve permitir que ele 
# consulte estoque, atualize o estoque, e adicione novos produtos, para 
# adicionar novos produtos ele deve conter um nome, uma rápida 
# descrição do produto que conterá um tipo (higiene, alimento, produtos 
# para casa e etc) e um subtipo (ex: alimento: frios, carne, legumes, 
# massas, etc), além de conter um preço e um código, dentro dos produtos 
# desse mercado o preço deverá ter a possibilidade de ser alterado mas as 
# demais propriedades dele não podem ser alteradas. 

#  /--------------Parte 4: 
# Criação da nota fiscal. 
# Na nota fiscal todos os produtos devem ser impressos na tela com o 
# seu valor e ao final com o valor total e o valor dos impostos sendo: 3 
# tipos de imposto, 5% nacional, 8% estadual e 12% municipal. 
# Os valores de cada imposto devem ser apresentados e mostrar o 
# cálculo do valor total da compra. 

#  /--------------Sugestão: Já deixe alguns produtos cadastrados para realizar os testes 
# no seu sistema.