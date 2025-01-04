
import os
import sys
modules = os.path.abspath("../")
sys.path.append(modules)
from bip32 import *

dicionario = []
for i in open('dicionario.txt').readlines():
    dicionario.append(i[:-1])


def words_in_positions(texto, positions):
    resp = []
    words = ''
    for i in positions:
        resp.append(str(i) + " - " + texto[i-1])
        if texto[i-1] in dicionario:
            words = words + texto[i-1] + " "

    words = words[:-1]
    return words


def main():
    wallet = "1K4ezpLybootYF23TM4a8Y4NyP7auysnRo"
    texto1 = "witch collapse practice feed shame open despair creek road again ice least"

    texto1 = texto1.split()
    #print(texto1)
    words = ''
    cont = 0

    for pos_0 in dicionario:
        if pos_0[0] == 'w':
            texto1[0] = pos_0
            for pos_1 in dicionario:
                if pos_1[0] == "c":
                    texto1[1] = pos_1
                    for pos_4 in dicionario:
                        if pos_4[0] == "s":
                            texto1[4] = pos_4
                            for pos_11 in dicionario:
                                if pos_11[0] == "l":
                                    texto1[11] = pos_11
                                    for i in texto1:
                                        words = words + " " + i
                                    #words = words[:-1]
                                    #print(words)
                                    cont+=1

                                    if cont % 1000 == 0:
                                        print(words)

                        
                                    resp = gera_dados_carteira(words, "")
                                    if resp:
                                        for wallets in resp:
                                            print(wallets)
                                            if wallets == wallet:
                                                print("ACHEI!")
                                    
                                    words = ''



if __name__ == "__main__":
    main()