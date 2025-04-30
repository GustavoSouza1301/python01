def imprime_nome(nome):
    print(f"Nome:{nome}")

def solicitarNome():
    nome = input("Digite o seu nome: ")
    return nome

def piranmide(num):
    for x in range(1, num + 1, 1):
        for i in range(0, x):
            print(x, end=" ")
        print()

def contaVogais(texto):
    vogais = "aeiouAEIOU"
    quant = 0
    for i in range(0, len(texto), 1):
        if texto[i] in vogais:
            quant += 1
    print(quant)

def estoque(produto, quant, valorProduto):
    valorTotal = quant * valorProduto
    print(valorTotal)