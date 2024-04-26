    #Média Escolar

    unidade1 = float (input ("Informe a sua nota da 1ª UNIDADE: "))
    unidade2 = float (input ("Informe a sua nota da 2ª UNIDADE: "))
    unidade3 = float (input ("Informe a sua nota da 3ª UNIDADE: "))

    soma =  unidade1+unidade2+unidade3
    media = soma/3

    if media >= 7:
        print("VOCÊ FOI APROVADO! Sua média foi: %.1f" %media)
    else:
        print("VOCÊ FOI REPROVOU! Sua média foi: %.1f" %media)
                      
