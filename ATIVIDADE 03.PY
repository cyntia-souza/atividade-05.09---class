while True:
    usuario = input("digite o nome de usuario").strip()
    senha = input("digite sua senha").strip()

    if senha == usuario:
        print("erro: a senha não pode ser igual ao nome de usuario.\n")
    elif usuario in senha:
        print("erro: a senha não pode contar o nome de usuario.\n")
    else:
        print("\n usuario e senha cadastrados com sucesso!")
        break
