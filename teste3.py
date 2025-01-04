
import os
import sys
modules = os.path.abspath("../")
sys.path.append(modules)
import random
from itertools import permutations
from bip32 import *
import math
import re


bip_dictionary = []
with open('dicionario.txt') as file:
    for line in file.readlines():
        bip_dictionary.append(line[:-1])


def dictionary_words_in_text(file_name, bip_dictionary):
    dictionary_words = []
    with open(file_name) as file:
        for line in file.readlines():
            word_list = line.split()
            for word in word_list:
                if re.sub(r'[^a-zA-Z0-9\s]', '',word).lower() in bip_dictionary:
                    dictionary_words.append(re.sub(r'[^a-zA-Z0-9\s]', '',word).lower())

    #print(dictionary_words)
    return(dictionary_words)

    

def main():

    phrases = []
    text = ''
    coinmonk = '1K4ezpLybootYF23TM4a8Y4NyP7auysnRo'
    found = False
    cont = 0


    ####Carteira a ser validada####
    WALLET = coinmonk
    
    ####Arquivo a ser validado####
    TEXTO = "texto_puro.txt"
    #TEXTO = "palavras_em_negrito.txt"
    #TEXTO = "texto_exemplo.txt"

    list_of_words = dictionary_words_in_text(TEXTO, bip_dictionary)

    for phrase in range(len(list_of_words) - 11):
    #for comentado para tentar também com tamanho 24
    #for phrase in range(len(list_of_words) - 23):
        for single_word in list_of_words[phrase:phrase + 12]:
        #for comentado para tentar também com tamanho 24    
        #for single_word in list_of_words[phrase:phrase + 24]:
            text = text + single_word + " "
        text = text[:-1]
        print(text)
        
        
        cont+=1
        resp = gera_dados_carteira(text, "")
        #print(resp)
        text = ''
        #print(cont)
        if resp:
            #print(resp)

            for wallets in resp:
                print(wallets)
                ######Excolhe a carteira que deverá ser utilizada######
                if wallets == WALLET:
                    print("-----ACHEI!-----")
                    print(wallets)
                    found = True
    
                    
        #else:
        #    print(resp)

        if found:
            break

    print(len(list_of_words))
    
    
if __name__ == "__main__":
    main()