import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def encrypt_file():
    # Cargar llave pública desde archivo PEM
    public_key_path = os.path.join("keypair", "keylogger_public.pem")
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    
    # Leer el archivo de entrada
    input_path = os.path.join("test", "in.txt")
    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
    
    # Crear el directorio de salida si no existe
    output_path = os.path.join("test", "encrypted_output.txt")
    with open(output_path, "wb") as output_file:
        for line in lines:
            # Cifrar cada línea usando la llave pública
            encrypted_data = public_key.encrypt(
                line.encode('utf-8'),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            # Escribir los datos cifrados en el archivo de salida
            output_file.write(encrypted_data + b'\n')

if __name__ == "__main__":
    encrypt_file()
    print("Encryption completed. Output saved to test/encrypted_output.txt")
