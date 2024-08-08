from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.keys import Address
from bitcoinlib.keys import HDKey
from bitcoinlib.keys import Key
from bitcoinlib.wallets import Wallet
from bitcoinlib.keys import Signature
import bitcoinlib

def gera_dados_carteira(words):

    try:

        #Detect Language
        #ret = Mnemonic().detect_language('faint lonely scale gate camera shoulder adult game medal language payment')

        #words = 'chunk gun celery million wood kite tackle twenty story episode raccoon dutch'
        #words = Mnemonic().generate(strength=128)
        #print(words)
        entropy = Mnemonic().to_entropy(words)
        #print('Entropy: ', entropy)
        #print(entropy.hex())
        seed = Mnemonic().to_seed(words)
        #print('Seed: ', seed)
        #print(seed.hex())

        hd_key = HDKey.from_seed(seed)
        #print("HDKey: ", hd_key)
    
    
  

        paths = ["m/0/0", "m/44'/0'/0'/0/0", "m/49'/0'/0'/0/0", "m/84'/0'/0'/0/0"]


        for i in paths:
            key = hd_key.subkey_for_path(i)
            #print(type(key)) 
            #print(key.info())
            #print(key.as_json())
            print(i)
            print("ADRRESS: ", key.address())
            print("ADRRESS: ", key.address(script_type='p2pkh'))
            print("ADRRESS: ", key.address(script_type='p2pkh', encoding='bech32'))
            print("ADRRESS: ", key.address(script_type='pp2sh'))
            print("ADRRESS: ", key.address(script_type='pp2sh', encoding='bech32'))
            print("PUBLIC_KEY: ", key.public())
            print("WIF: ",key.wif_key())
            print("\n")
    
    except Exception as e:
        print("Error Code: ", e)
        return False
    
    return True

