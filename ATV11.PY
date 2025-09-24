n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

# Garante que n1 seja o menor
if n1 > n2:
    n1, n2 = n2, n1

# Calcula a soma dos ímpares no intervalo
soma_impares = sum(i for i in range(n1, n2 + 1) if i % 2 != 0)

print(f"\nA soma de todos os números ímpares entre {n1} e {n2} é: {soma_impares}")