from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.keys import Address
from bitcoinlib.keys import HDKey
from bitcoinlib.keys import Key
from bitcoinlib.wallets import Wallet
from bitcoinlib.keys import Signature
import bitcoinlib


def gera_mnemonic(word):
    words = Mnemonic().to_mnemonic(word)
    print(words)

def gera_dados_carteira(words, passwd):

    try:
        entropy = Mnemonic().to_entropy(words)
        seed = Mnemonic().to_seed(words, password=passwd)
        #print(seed.hex())
        hd_key = HDKey.from_seed(seed)
    except Exception as e:
        #print("Error Code: ", e)
        return False
    
    
    #paths = ["m/0/0", "m/44'/0'/0'/0/0", "m/49'/0'/0'/0/0", "m/84'/0'/0'/0/0"]
    paths = ["m/0/0", "m/44'/0'/0'/0/0", "m/49'/0'/0'/0", "m/84'/0'/0'/0/0"]
    info = []

    for i in range(len(paths)):
        key = hd_key.subkey_for_path(paths[i])
        #print(type(key)) 
        #print(key.info())
        #print(key.as_json())
        #print(i)
        #print("ADRRESS: ", key.address())
        #print("ADRRESS: ", key.address(script_type='pp2sh', encoding='bech32'))
        #print("PUBLIC_KEY: ", key.public())
        #print("WIF: ",key.wif_key())
        #print("\n")
        info.append(key.address())
        info.append(key.address(script_type='pp2sh', encoding='bech32'))
        info.append(key.wif_key())

    
    return info

