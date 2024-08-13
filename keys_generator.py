import ecdsa
import hashlib
import base58
import base64

# Gerar uma chave privada aleatória (256 bits)
def generate_private_key():
    pk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    return pk


# Derivar a chave pública a partir da chave privada
def get_public_key(private_key):
    return private_key.verifying_key.to_string(), private_key.verifying_key.to_string("compressed")

# Gerar o endereço Bitcoin a partir da chave pública
def generate_bitcoin_address(public_key):
    # Calcular o hash SHA-256 da chave pública
    sha256_hash = hashlib.sha256(public_key).digest()
    
    # Calcular o RIPEMD-160 do hash SHA-256
    ripe_hash = hashlib.new('ripemd160', sha256_hash).digest()
    
    # Adicionar o byte de versão (0x00 para mainnet)
    versioned_ripe_hash = b'\x00' + ripe_hash
    
    # Calcular o checksum (SHA-256 de SHA-256 dos bytes anteriores)
    checksum = hashlib.sha256(hashlib.sha256(versioned_ripe_hash).digest()).digest()[:4]
    
    # Concatenar o endereço base58 com o checksum
    bitcoin_address = versioned_ripe_hash + checksum
    
    # Codificar para base58 (endereço Bitcoin final)
    bitcoin_address_base58 = base58.b58encode(bitcoin_address).decode('utf-8')
    
    return bitcoin_address_base58



# Função principal para gerar chave privada, chave pública e endereço Bitcoin
def main():
    # Gerar uma chave privada
    private_key_random = generate_private_key()
    print("Chave privada aleatoria: ", private_key_random)
    print(f"Chave privada aleatoria (hex): {private_key_random.to_string().hex()}")
    print("\n")
    #print(type(private_key))

    hex_key = "efa02138be2ee68881a8f2f9b87471e397e373211238b9077feeb73ad5fd19b8"
    private_key_bytes = bytes.fromhex(hex_key)
    private_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    

    # Derivar a chave pública
    public_key, public_key_compressed = get_public_key(private_key)
    
    # Gerar o endereço Bitcoin a partir da chave pública
    bitcoin_address = generate_bitcoin_address(public_key)
    bitcoin_address_compressed = generate_bitcoin_address(public_key_compressed)
    
    # Exibir resultados
    print("Chave privada informada: ", private_key)
    print(f"Chave Privada (hex): {private_key.to_string().hex()}")
    print(f"Chave Pública (hex): {public_key.hex()}")
    print(f"Chave Pública Comprimida: {public_key_compressed.hex()}")
    print(f"Endereço Bitcoin: {bitcoin_address}")
    print(f"Endereço Bitcoin Comprimido: {bitcoin_address_compressed}")
    print("\n")



if __name__ == "__main__":
    main()