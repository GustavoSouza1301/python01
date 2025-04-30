from biblioteca import estoque

nome = input("Digite o nome do produto: ")
valor = float(input("Qual o valor do produto: "))
quantidade = int(input("Quantos  tem? "))

retorno = estoque(nome,quantidade,valor)

print(retorno)