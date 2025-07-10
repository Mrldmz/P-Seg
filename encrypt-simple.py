import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def encrypt_file():
    # Cargar llave pública desde archivo PEM
    public_key_path = os.path.join("keypair", "keylogger_public.pem")
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    
    # Leer el archivo de entrada completo
    input_path = os.path.join("test", "in.txt")
    with open(input_path, "rb") as input_file:
        content = input_file.read()
    
    # RSA-2048 con OAEP puede cifrar hasta ~190 bytes por bloque
    max_chunk_size = 190
    encrypted_blocks = []
    
    # Dividir contenido en bloques y cifrar
    for i in range(0, len(content), max_chunk_size):
        chunk = content[i:i + max_chunk_size]
        encrypted_chunk = public_key.encrypt(
            chunk,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encrypted_blocks.append(encrypted_chunk)
    
    # Guardar todos los bloques cifrados concatenados
    output_path = os.path.join("test", "encrypted_output.txt")
    with open(output_path, "wb") as output_file:
        for encrypted_block in encrypted_blocks:
            output_file.write(encrypted_block)

if __name__ == "__main__":
    encrypt_file()
    print("Encryption completed. Output saved to test/encrypted_output.txt")
