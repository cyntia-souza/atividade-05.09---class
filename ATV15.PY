# Entrada do número
num = int(input("Digite um número inteiro: "))

# Inicializa soma dos divisores
soma_divisores = 0

# Verifica todos os divisores (exceto o próprio número)
for i in range(1, num):
    if num % i == 0:
        soma_divisores += i

# Verificação final
if soma_divisores == num and num != 0:
    print(f"{num} é um número perfeito!")
else:
    print(f"{num} não é um número perfeito.")