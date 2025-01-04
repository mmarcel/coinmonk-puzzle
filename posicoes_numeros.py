import os
import sys
modules = os.path.abspath("../")
sys.path.append(modules)
from bip32 import *
from teste3 import dictionary_words_in_text

bip_dictionary = []
with open('dicionario.txt') as file:
    for line in file.readlines():
        bip_dictionary.append(line[:-1])

TEXTO = "texto_editado.txt"
words = []
palavras = ""

list_of_words = dictionary_words_in_text(TEXTO, bip_dictionary)

#posicoes = [1,16,20,36,42,50,60,70,81,98,107,117,121,138,147,157,161,178,188,190,202,210,220,230]
posicoes = [1,6,10,16,22,30,40,50,51,58,67,77,81,88,97,107,111,118,128,130,132,140,150,159]
#print(len(posicoes))
print(len(list_of_words))
print(list_of_words[-1:])

while (len(list_of_words) > 24):
    print(len(list_of_words))
    #print(list_of_words)

    for i in posicoes:
        #print(list_of_words[i])
        words.append(list_of_words[i-1])
    #print(words)

    for j in words:
        palavras = palavras + " " + j
        
    print("Palavras: ",palavras)

    resp = gera_dados_carteira(palavras, "")
    print(resp)
    text = ''
    #print(cont)
    if resp:
        print(resp)

        for wallets in resp:
            print(wallets)
            ######Excolhe a carteira que deverá ser utilizada######
            if wallets == WALLET:
                print("-----ACHEI!-----")
                print(wallets)
                found = True

    list_of_words.pop(0)
    palavras = ""
    words = []
            
#else:
#    print(resp)



