while True: 
  try: 
    nota = float(input("digite uma nota entre 0 e 5:"))
    if 0 <= nota <= 5:
        print(f"nota valida inserida: {nota}")
        break
    else:
        print("erro: deve estar entre 0 e 5")
  except ValueError:
   print("erro: voce deve digitar um numero")