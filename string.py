#print ('Está é uma string');

s = "Alo Mundo"
print(s[4])

#transforma string em list 
L= list("Alo Mundo")
print (L)

#junta a string novamente
string2 = "".join (L)
print (string2)

#verifica o primeiro caractere de uma string 
gisele = "Gisele é uma pessoa legal"
print(gisele.startswith("Gise"))

#verificar se existe no final da string 
print (gisele.endswith("E"))

#converte toda a string em maiusculo
lucas = "Lucas é meu namorado"
print (lucas.upper())

#converte a string em minusculo
print (lucas.lower())

#retira os espaços em branco da string
print (lucas.strip())

#descobrir se tem um elemento ou não
print("Lucas" in lucas)
print("Gisele" not in lucas)

#localiza a posição do caractere na string
print (lucas.find("l"))

#localiza a posição do caractere no final da string
print (lucas.rfind("s"))

#contar a quantidade de ocorrencias de um caracter
print (lucas.count("g"))

#contar a quantidade de ocorrencias de uma palavra
print (lucas.count("namorado"))

#verifica se a string é numerica
print (lucas.isdigit())