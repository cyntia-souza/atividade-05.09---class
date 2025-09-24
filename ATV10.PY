# Entrada dos dois números
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

# Garante que n1 seja o menor
if n1 > n2:
    n1, n2 = n2, n1

# Cria a lista de pares
pares = [i for i in range(n1, n2 + 1) if i % 2 == 0]

print(f"\nNúmeros pares entre {n1} e {n2}:")
print(pares)
