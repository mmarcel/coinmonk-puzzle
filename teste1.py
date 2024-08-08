
from bip32 import *

palavras = []
for i in open('palavras.txt').readlines():
    palavras.append(i[:-1])



def main():

    texto1 = "the beauty of trithemian seeds is that they hide in plain sight if you ve read this far you ve read every word required to access a wallet with .03 BTC good luck"
    texto1_in_palavras = ''

    texto1 = texto1.split()
    

    for i in texto1:
        if i in palavras:
            #print("Tem: ", i)
            texto1_in_palavras = texto1_in_palavras + " " + i

    texto1_in_palavras = texto1_in_palavras[1:]
    print(texto1_in_palavras)
    gera_dados_carteira(texto1_in_palavras)





if __name__ == "__main__":
    main()