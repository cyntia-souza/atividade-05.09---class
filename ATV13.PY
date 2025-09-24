positivos = 0
negativos = 0
zeros = 0

for i in range(8):
    num = int(input(f"Digite o {i+1}º número inteiro: "))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print("\nResultados:")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Zeros digitados: {zeros}")