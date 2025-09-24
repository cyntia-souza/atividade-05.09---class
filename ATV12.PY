numero = int(input("Digite o número para a tabuada: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

print(f"\nTabuada do {numero} de {inicio} até {fim}:\n")

# Garante que o loop funcione mesmo se inicio > fim
if inicio <= fim:
    for i in range(inicio, fim + 1):
        print(f"{numero} x {i} = {numero * i}")
else:
    for i in range(inicio, fim - 1, -1):
        print(f"{numero} x {i} = {numero * i}")