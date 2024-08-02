// Import necessary libraries
const bip39 = require("bip39");
const bitcoin = require("bitcoinjs-lib");
const HDKey = require("hdkey");
const CoinKey = require("coinkey");



function resultado(path) {
  const child = hdKey.derive(path);

  // Create a CoinKey from the derived child private key and specify the Bitcoin network
  const coinKey = new CoinKey(child.privateKey, bitcoin.networks.bitcoin);

  // Prepare an object with address, path, private key, and Wallet Import Format (WIF) key
  const info = {
    address: coinKey.publicAddress,          // Bitcoin public address
    path,                                    // BIP44 path
    privateKey: coinKey.privateKey.toString("hex"), // Private key in hexadecimal
    WIF: coinKey.privateWif,                 // Wallet Import Format (WIF) private key
  };

  // Log the information to the console
  //console.info(info);
  return info

}

// Replace 'your 12-word mnemonic here' with your actual 12-word mnemonic.
const mnemonic = "asset trial load escape symbol story bomb picnic river aerobic mystery honey"

// Convert the mnemonic to a seed
const seed = bip39.mnemonicToSeedSync(mnemonic);

// Create an HD wallet key from the seed
const hdKey = HDKey.fromMasterSeed(Buffer.from(seed, "hex"));

// Define the BIP44 path for Bitcoin (m/44'/0'/0'/0/0)

//BIP32 - m/0/0
//BIP44 - m/44'/0'/0'/0/0
//BIP49 - m/49'/0'/0'/0/0
//BIP84 - m/84'/0'/0'/0/0
//BIP141 - m/0/0

const paths = ["m/0/0", "m/44'/0'/0'/0/0", "m/49'/0'/0'/0/0", "m/84'/0'/0'/0/0"]
const path = "m/0/0";

for (let i = 0; i < paths.length; i++) {
  console.log(paths[i])
  ret = resultado(paths[i])
  console.log(ret)
}




