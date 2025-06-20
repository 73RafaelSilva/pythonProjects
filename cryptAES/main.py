from base64 import b64encode, b64decode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import hashlib
import pickle

def encrypt(plain_text, key):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the key
    private_key = hashlib.scrypt(key.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def decrypt(enc_dict, key):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    # generate the private key from the key and salt
    private_key = hashlib.scrypt(key.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)
    return decrypted


def main():

    with open("dado.png", "rb") as imagem:
        bytesImagem = imagem.read()

    textImagem = str(bytesImagem)
    print(textImagem)

    key = input("key: ")

    # First let us encrypt secret message
    encrypted = encrypt(textImagem, key)
    #Salva arquivo serializado no pickle
    objetoCifradoSerializado = pickle.dumps(encrypted)

    #cria nova imagem com texto cifrado
    with open("dadoCifrado.png", "wb") as imagem:
        imagem.write(objetoCifradoSerializado)

    #Processo Inverso....

    # Let us decrypt using our original key
    decrypted = decrypt(encrypted, key)
    #cria nova imagem com imagem cifrada
    objetoDeifradoSerializado = pickle.dumps(decrypted)
    with open("dadoDecifrado.png", "wb") as imagem:
        imagem.write(objetoDeifradoSerializado)

main()