
import random
from itertools import permutations
from bip32 import *
import math

dicionario = []
with open('dicionario.txt') as file:
    for word in file.readlines():
        dicionario.append(word[:-1])


def main():

    #texto = "what if you could embed your net worth in a story"
    #texto = "my grandfather known to me as ye-ye was born into a large well to do merchant class family in the early 1930’s during a troubled time in china"
    #texto = "a decade after the dissolution of dynastic imperialism that lasted over 2000 years china in the 1920’s was fighting to find its identity among a massive cultural shift warlordism and civil war in an increasingly global world"
    #texto = "tensions were brewing while my ye-ye grew up in what he describes as an idyllic childhood despite unsettling clues of a quietly turbulent and changing time he was the eldest of six siblings born to a mother of bound feet and a successful merchant father who would disappear most afternoons to frequent opium dens or as he called them tea houses"
    #texto = "thousands of years of changing dynastic rules ingrained cautions of inflationary currency in chinese psyche and most people during this time turned to gold as savings as well as an informal medium of exchange"
    #texto = "my ye-ye remembers a large wooden cabinet in the main sitting room of his house where a hidden trap door was installed by his father"
    #texto = "in it held the majority of his familys wealth in gold and silver the rest was hidden in the ground under his mother wooden wardrobe"
    #texto = "at the time of my childhood a tael of gold could purchase 40 bags of fine flour at 40 lbs each towards the peak of civil unrest a passage on boat from the mainland to taiwan could cost up to 10 taels of gold"
    #texto = "by the time my turned eighteen the japanese were retreating and the temporary truce between two clashing political ideals was falling apart the second japo sino war impoverished both sides while the kuomintang increased inflation to pay its debts from civil war funding the communist party of china  was being energized by the masses of peasants looking for a revolution."
    #texto = "driving the rhetoric of the communist cause was the underlying distrust and bitterness of wealth held by the upper classes for centuries and the promise from the to redistribute lands to the people once the war was over lands owned by families like my"
    #texto = "journey swift little eagle parade enough obtain virtual sausage gym stone erase"
    #texto = "seed phrases are often stored in a format that signals the storage of wealth"
    #5 / texto = "if found a numbered list of seed phrases can be recognized as a password to an undefined amount of money"
    #3 + texto = "whether to a government regime or to thieves along the journey of migration cryptocurrency touchpoints belie one of the major characteristics of bitcoin undetectability and inconfiscatabilty"
    #9 + texto = "seed phrases are often stored in a format that signals the storage of wealth if found a numbered list of seed phrases can be recognized as a password to an undefined amount of money" 
    #12 - texto = "seed phrases are often stored in a format that signals the storage of wealth if found a numbered list of seed phrases can be recognized as a password to an undefined amount of money whether to a government regime or to thieves along the journey of migration cryptocurrency touchpoints belie one of the major characteristics of bitcoin undetectability and inconfiscatabilty"
    #7 / texto = "carrying a list of seed phrases along your journey could be considered suspect behavior and put any individual at risk"
    #9 - texto = "even the average person who stores their seed phrases in a single physical location could have their funds stolen if they are found by someone familiar with the process of restoring from backup phrases"
    #5 / texto = "fishing freshwater bends and saltwater coasts rewards anyone feeling stressed resourceful anglers usually find masterful leapers fun and admit swordfish rank overwhelming any day"
    #4 / texto = "for thousands of years wealth and information have been carried through different mediums from song and poetry to books diaries stories and art"
    #7 / texto = "what if we embedded our seed phrases into stories to develop monetary safety and sovereignty for people around the world"
    #11 / texto = "for thousands of years wealth and information have been carried through different mediums from song and poetry to books diaries stories and art what if we embedded our seed phrases into stories to develop monetary safety and sovereignty for people around the world"
    #texto = "despite excelling as a method of developing monetary sovereignty and transporting wealth in economic crises bitcoin falls short in a few areas"
    #texto = "if recognized by regimes or thieves public addresses private keys backup seed phrases or hardware wallets can be seen as a notable sign of wealth making anyone vulnerable to theft confiscation or extortion"
    #11 - texto = "it is inevitable that the border security personnel of collapsing regimes will be trained to identify cryptocurrency touchpoints to detect and control value flows and emigration preventing economic refugees from leaving safely with what value they have left"
    #texto = "while bitcoin itself is intangible in order for us to engage with the network we have to interact with points of contact along the way"
    #texto = "backup seed phrases are mnemonic devices used to backup and restore access to wallets"
    #texto = "private keys effectively the password to your account generated by cryptographic hashing algorithms are incredibly challenging if not impossible to memorize and their format speaks to the nature of a private key"
    #texto = "BIP-39 seed phrases were implemented to create an english language backup to be kept entirely offline these are used by the majority of trusted wallet providers to backup and restore access to accounts instead of needing addresses together with private keys only the seed phrases are required to access an account"
    #texto = "how can we best enable the safe migration of people and their value"
    #texto = "in tumultuous circumstances steganography becomes of critical importance many techniques having been developed to secure communications in times of war"
    #texto = "a null cipher is a specific form of steganography where unencrypted messages are stored within a larger message which conceals the secondary meaning"
    #texto = "witch collapse practice feed shame open despair creek road again ice least"
    #11 - texto = "in this method a short story is written with true and decoy seed phrases interspersed among a handwritten piece of text that would fit well in a notebook"
    #texto = "these should be written on a different page to remove any connection between the text and the numbers"
    #texto = "there are many ways to approach the development of trithemian seeds some examples could include"
    #6 - texto = "storing seed phrases in a numbered list would put anyone at risk especially economic refugees migrants or travelers seeds can instead be embedded in poetry stories notebooks or works of art"
    #8 - texto = "a trithemian seed is a list of cryptocurrency backup seed phrases stored in an innocuous body of writing such as a poem story or letter"
    #texto = "faint lonely scale gate camera shoulder adult game medal language payment"
    #texto = "such an asset to be represented by an experienced and mature lawyer particularly when you have a trial in front of the supreme court of the USA load your argument with logic and do not provide ways to escape"
    #texto = "symbol of cultural diversity should be used as often as possible in order to support the story our client clearly did not make that complex and improvised bomb himself they were on their way to his friend picnic by the river when he noticed a suspicious person pretending to do aerobic exercises he immediately pointed it out to his friends their whereabouts aren't a mystery during the attack they were ordering ginger tea with honey to bring to the picnic"
    #10 - texto = "this method eliminates the need for a number pair heightening strength at the cost of complexity in this case a geographic landmark is chosen that relates to a plot built around the given seed phrases"
    #8 - texto = "the GPS coordinates of this landmark dictate the placement of the seed phrases among the body of text to maintain relatively easy dispersal with slight variation every digit read increases by ten so 21.493021 translates to"
    #8 - texto = "these examples are not necessarily meant to be cryptographically secure or uncrackable under close examination they are intended to store seed phrases in a way that prevents its viewers from even thinking to search deeper into its meaning"
    #12 - texto = "if these were sent as a letter carried as a notebook or both few people would have the reason and effort to investigate the sheer volume of information only you know which story contains your wealth"
    #11 - texto = "it can be easy to overlook the point of bitcoin living in a country where people trust their government what happens to those who can’t What has happened to those who couldn’t it is truly a privilege to be unaware of the importance of trust"
    #texto = "it is truly a privilege to be unaware of the importance of trust"
    #texto = "the potential of cryptocurrencies isnt limited to the speed of transactions or speculation but rather in redefining financial autonomy by enabling people to be free to make their own decisions"
    #texto = "the beauty of trithemian seeds is that they hide in plain sight if you have read this far you have read every word required to access a wallet with .03 BTC good luck"
    #texto = "the beauty of trithemian seeds is that they hide in plain sight"
    #texto = "if you have read this far you have read every word required to access a wallet with 03 BTC good luck"
    #texto = "system control key private phrase seed ancient poem over"
    texto = "first badge goose soup learn unique"

    
    
    words = ''
    passwd = ''
    coinmonk = '1K4ezpLybootYF23TM4a8Y4NyP7auysnRo'
    teste_iancoleman = "164npgnZ3j61DWoWmeyh8XwAsMhqKdW29r"

    palavras_in_dicionario = []
    cont = 0

    texto_lista = texto.split()

    for i in texto_lista:
        if i in dicionario:
            palavras_in_dicionario.append(i)
            

    print(len(palavras_in_dicionario), " - ", math.factorial(len(palavras_in_dicionario)), " combinações")
    print(palavras_in_dicionario)

    if len(palavras_in_dicionario) % 3 != 0:
        exit()

    perms = permutations(palavras_in_dicionario)

    achei = False
    for i in perms:
        cont+=1
        #print(i)
        for j in i:
            words = words + " " + j

        words = words[1:]
        #print(words)

        resp = gera_dados_carteira(words, passwd)
        #print(resp)

        if resp:
            for wallets in resp:
                #print(k)
                #print(words)
                if wallets == teste_iancoleman:
                    print("ACHEI!")
                    print(words)
                    print(wallets)
                    achei = True
                    break
            if achei:
                break

        if cont % 1000 == 0:
            print(cont, " ", words)

#Imprime todas as combinações
#        print(cont, " ", words)

        words = ''
    
if __name__ == "__main__":
    main()