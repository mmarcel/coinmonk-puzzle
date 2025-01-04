
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

    texto1 = "the faint lines across the lonely expanse make scale hard to determine as I walk towards the gate I sling my camera over my shoulder and prepare to enter the old palace The door pushes open easily and I walk into the courtyard no adult in sight I place my camera on the table and get to work searching through the waste As I dust off an ancient board game something shiny catches my eye I reach towards the cupboard and pick up a gold medal Upon closer inspection I notice an inscription that seems to resemble a foreign language I pocket the trinket with the hope that this might make for a good enough payment at the border Any valuable will do"

    texto1 = texto1.split()
    #print(texto1)

    for palavra in dicionario:
        texto1[112] = palavra
   

        posicoes1 = [2,6,9,18,22,25,45,70,86,100,113,116]


        resp1 = []
        geral = []
        wallet = "1K4ezpLybootYF23TM4a8Y4NyP7auysnRo"

        words1 = words_in_positions(texto1, posicoes1)
        print(words1)

        print("\n")
        resp = gera_dados_carteira(words1, "")
        if resp:
            for wallets in resp:
                print(wallets)
                if wallets == wallet:
                    print("ACHEI!")
        else:
            print(resp)



if __name__ == "__main__":
    main()