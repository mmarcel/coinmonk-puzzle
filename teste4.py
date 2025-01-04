import os
import sys
modules = os.path.abspath("../")
sys.path.append(modules)
from generators import *
from bip32 import *

ret = gera_dados_carteira_privatekey("6673bbbf0d84f102110615189c49fea461738b0b805046df2fc5e5333ed04532")
print(ret)

words = "witch collapse practice feed shame open despair creek road again ice least"
print(words)
retorno = gera_dados_carteira(words, "")
print(retorno)