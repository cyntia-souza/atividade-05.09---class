while True:
    nome = input("digite seu nome(minimo 4 caracteres): ").strip()
    if len(nome) >= 4:
        break
    else: 
        print("error: o nome deve ter pelo menos 4 caracters.")

while True:
    idade_str = input("Digite sua idade (entre 1 e 100): ").strip() 
    if idade_str.isdigit():  
        idade = int(idade_str)
        if 1 <= idade <= 100:
            break
        else:
            print("Erro: a idade deve estar entre 1 e 100.")
    else:
        print("Erro: digite um número inteiro válido para a idade.")

while True:
        bruto = input("Digite seu salário (valor positivo, ex: 3500,75 ou R$ 3.500,75): ")
        try:
            
            salario = float(bruto.replace("R$", "").replace(" ", "").replace(",", "."))
            if salario > 0:
                "return" 'salario'
            else:
                print(" Salário deve ser maior que zero.")
        except ValueError:
            print(" Não entendi o valor. Exemplos: 3500,75 | 3500.75 | R$ 3.500,75")

while True:
    genero = input ("digite seu genero ( f - feminino, m  - masculino, o - outro): ")
    if genero in ("f", "m", "o"):
        "return" 'genero' 
        print("genero invalido! use apenas 'f', 'm', 'o'. ")

while True:
        situacao = input("Digite sua situação empregatícia (e - empregado, d - desempregado, a - autônomo): ").strip().lower()
        if situacao in ("e", "d", "a"):
            'return' "situacao"
        print(" Situação inválida! Use apenas 'e', 'd' ou 'a'.")