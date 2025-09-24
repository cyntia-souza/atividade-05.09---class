produto = 1
soma = 0

for i in range(6):
    num = float(input(f"Digite o {i+1}º número: "))
    produto *= num
    soma += num

media = soma / 6

print(f"\nProduto dos números: {produto}")
print(f"Média aritmética: {media}")