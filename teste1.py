
import os
import sys
modules = os.path.abspath("../")
sys.path.append(modules)
from bip32 import *

palavras = []
for i in open('dicionario.txt').readlines():
    palavras.append(i[:-1])


def main():

    wallet = "1K4ezpLybootYF23TM4a8Y4NyP7auysnRo"

    texto = "asset trial load escape symbol story bomb picnic river aerobic mystery honey"
    texto_in_palavras = ''

    texto = texto.split()
    

    for i in texto:
        if i in palavras:
            #print("Tem: ", i)
            texto_in_palavras = texto_in_palavras + " " + i

    texto_in_palavras = texto_in_palavras[1:]
    print(texto_in_palavras)
    ret = gera_dados_carteira(texto_in_palavras, "")
    print(ret)
    if wallet in ret:
        print("ACHEI!!!")


if __name__ == "__main__":
    main()