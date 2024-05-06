peixes = float(input("Digite o peso dos peixes (em quilogramas): "))

limite = 50
if peixes > limite:
    excesso = peixes - limite
    multa = excesso * 4
    print("João excedeu o limite de peso em ", excesso, "kg.")
    print("Valor da multa a ser paga por João: R$", multa)
else:
    print("João não excedeu o limite de peso. Não há multa a ser paga.")
