dicionario = []
with open('titulos.txt') as file:
    for word in file.readlines():
        #print(word, " - ", len(word))
        dicionario.append(word[:-1])

for i in dicionario:
    print(i, " - ", len(i))