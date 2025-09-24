while True:
    try:
        # Entradas da cidade A
        pop_a = int(input("Digite a população inicial da cidade A: "))
        taxa_a = float(input("Digite a taxa de crescimento anual da cidade A (%): "))

        # Entradas da cidade B
        pop_b = int(input("Digite a população inicial da cidade B: "))
        taxa_b = float(input("Digite a taxa de crescimento anual da cidade B (%): "))

        # Validação
        if pop_a <= 0 or pop_b <= 0 or taxa_a <= 0 or taxa_b <= 0:
            print("❌ Todos os valores devem ser positivos. Tente novamente.\n")
            continue

        # Convertendo taxas para decimal
        taxa_a /= 100
        taxa_b /= 100

        anos = 0

        # Simulação ano a ano
        while pop_a < pop_b:
            pop_a += pop_a * taxa_a
            pop_b += pop_b * taxa_b
            anos += 1

        print(f"\n Serão necessários {anos} anos para a cidade A ultrapassar ou igualar a população da cidade B.")
        print(f"População final da cidade A: {int(pop_a)} habitantes")
        print(f"População final da cidade B: {int(pop_b)} habitantes\n")

    except ValueError:
        print("❌ Entrada inválida! Digite apenas números.\n")
        continue

    # Perguntar se o usuário deseja repetir
    repetir = input("Deseja realizar outro cálculo? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa. Até mais!")
        break