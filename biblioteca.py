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