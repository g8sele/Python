altura = float(input("Digite sua altura (em metros): "))

sexo = input("Digite 'M' se for homem ou 'F' se for mulher: ")

if sexo.upper() == 'M':
    peso = (72.7 * altura) - 58
    print("Seu peso ideal é: ", peso, "em quilogramas")
elif sexo.upper() == 'F':
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é: ", peso, "em quilogramas")
else:
    print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
