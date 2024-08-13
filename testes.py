import os
import sys
modules = os.path.abspath("../")
sys.path.append(modules)
from bip.bip32 import *

#resp = gera_mnemonic("1808d35318ac7cb98b69ff9779b699d6a631f15e0b353ac89b7c4020774832ed")
#print(resp)


passwd = "nettik"
resp = gera_dados_carteira("blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room", passwd)
#resp = gera_dados_carteira("erase sausage virtual little gym eagle swift stone journey obtain parade")
print(resp)
