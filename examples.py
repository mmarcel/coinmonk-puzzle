
from bip32 import *

palavras = []
for i in open('palavras.txt').readlines():
    palavras.append(i[:-1])


def words_in_positions(texto, positions):
    resp = []
    words = ''
    for i in positions:
        resp.append(str(i) + " - " + texto[i-1])
        if texto[i-1] in palavras:
            words = words + texto[i-1] + " "

    words = words[:-1]
    return words


def main():

    texto1 = "the faint lines across the lonely expanse make scale hard to determine as I walk towards the gate I sling my camera over my shoulder and prepare to enter the old palace The door pushes open easily and I walk into the courtyard no adult in sight I place my camera on the table and get to work searching through the waste As I dust off an ancient board game something shiny catches my eye I reach towards the cupboard and pick up a gold medal Upon closer inspection I notice an inscription that seems to resemble a foreign language I pocket the trinket with the hope that this might make for a good enough payment at the border Any valuable will do"
    texto2 = "such an asset to be represented by an experienced and mature lawyer particularly when you have a trial in front of the supreme court of the USA load your argument with logic and do not provide ways to escape symbol of cultural diversity should be used as often as possible in order to support the story our client clearly did not make that complex and improvised bomb himself they were on their way to his friends picnic by the river when he noticed a suspicious person pretending to do aerobic exercises he immediately pointed it out to his friends their whereabouts arent a mystery during the attack they were ordering ginger tea with honey to bring to the picnic"

    texto1 = texto1.split()
    #print(texto1)
    texto2 = texto2.split()
    #print(texto2)

    posicoes1 = [2,6,9,18,22,25,45,70,86,100,114,116]
    posicoes2 = [3,18,28,39,40,56,67,77,80,90,104,114]

    resp1 = []
    resp2 = []
    geral = []

    words1 = words_in_positions(texto1, posicoes1)
    words2 = words_in_positions(texto2, posicoes2)


    print(words1)
    print(words2)
    #print(resp2)

    print("\n")
    #gera_dados_carteira(words1)
    gera_dados_carteira(words2)



if __name__ == "__main__":
    main()