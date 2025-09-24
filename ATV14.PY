num = int(input("Digite um número inteiro: "))

# Números menores que 2 não são primos
if num < 2:
    print(f"{num} não é um número primo.")
else:
    # Verificação de divisores
    eh_primo = True
    for i in range(2, int(num**0.5) + 1):  # só precisa testar até a raiz quadrada
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{num} é um número primo!")
    else:
        print(f"{num} não é um número primo.")