# Populações iniciais
pop_a = 90000
pop_b = 250000

# Taxas de crescimento (em decimal)
taxa_a = 0.035  # 3.5%
taxa_b = 0.012  # 1.2%

anos = 0

# Enquanto A não ultrapassar ou igualar B
while pop_a < pop_b:
    pop_a += pop_a * taxa_a
    pop_b += pop_b * taxa_b
    anos += 1

print(f"Serão necessários {anos} anos para a cidade A ultrapassar ou igualar a população da cidade B.")
print(f"População final da cidade A: {int(pop_a)} habitantes")
print(f"População final da cidade B: {int(pop_b)} habitantes")