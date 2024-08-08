
from bip32 import *

dicionario = []
for i in open('dicionario.txt').readlines():
    dicionario.append(i[:-1])



def main():

    texto = "time how can we best enable the safe migration of people and their value a trithemian seed is a list of cryptocurrency backup seed phrases stored in an innocuous body of writing such as a poem story or letter the beauty of trithemian seeds is that they hide in plain sight if you ve read this far you ve read every word required to access a wallet with .03 BTC good luck"

    words = ''
    palavras_in_dicionario = []

    texto_lista = texto.split()

    for i in texto_lista:
        if i in dicionario:
            #print("Tem: ", i)
            palavras_in_dicionario.append(i)
            

    print(len(palavras_in_dicionario))
    print(palavras_in_dicionario)

    for i in palavras_in_dicionario[:12]:
        words = words + " " + i

    words = words[1:]
    print(words)
    

    #words = "eternal inflict place dynamic motion furnace skirt act toss all opera boring network fit valley"
    #print(texto1_in_palavras)
    resp = gera_dados_carteira(words)
    


if __name__ == "__main__":
    main()