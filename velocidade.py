tamanhoArquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velInternet = float(input("Digite a velocidade do link de Internet (em Mbps): "))

velInternetSegun = velInternet / 8

downloadSegun = tamanhoArquivo / velInternetSegun

downloadMin = downloadSegun / 60

print("Tempo aproximado de download: ", downloadMin, "min.")
