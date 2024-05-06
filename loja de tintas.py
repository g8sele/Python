area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

litros = area / 3

quantidade = litros / 18
quantidade = int(quantidade) + 1 if quantidade % 18 != 0 else quantidade

total = quantidade * 80

print("Quantidade de latas de tinta necessárias:", quantidade)
print("Preço total das latas de tinta: R$", total)
