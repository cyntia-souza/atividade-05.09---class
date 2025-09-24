 #Inicializa o menor como None (ainda não definido)
menor = None

for i in range(7):
    num = int(input(f"Digite o {i+1}º número inteiro: "))

    if menor is None or num < menor:
        menor = num

print(f"\nO menor número digitado foi: {menor}")