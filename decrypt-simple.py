from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import os

def decrypt_file():
    # Rutas de archivos
    private_key_path = "keypair/keylogger_private.pem"
    encrypted_file_path = "test/encrypted_output.txt"
    decrypted_file_path = "test/decrypted_output.txt"
    
    try:
        # Cargar clave privada
        with open(private_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None
            )
        
        # Leer datos cifrados
        with open(encrypted_file_path, "rb") as encrypted_file:
            encrypted_content = encrypted_file.read()
        
        # RSA-2048 produce bloques de 256 bytes cada uno
        block_size = 256
        decrypted_data = []
        
        # Procesar cada bloque cifrado
        i = 0
        while i < len(encrypted_content):
            # Extraer bloque de 256 bytes
            if i + block_size <= len(encrypted_content):
                encrypted_block = encrypted_content[i:i+block_size]
                
                # Descifrar bloque
                decrypted_block = private_key.decrypt(
                    encrypted_block,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                
                decrypted_data.append(decrypted_block)
                i += block_size
            else:
                break
        
        # Concatenar todos los bloques descifrados
        decrypted_content = b''.join(decrypted_data).decode('utf-8')
        
        # Escribir datos descifrados
        with open(decrypted_file_path, "w", encoding='utf-8') as decrypted_file:
            decrypted_file.write(decrypted_content)
        
        print(f"File successfully decrypted to {decrypted_file_path}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"Decryption error: {e}")

if __name__ == "__main__":
    decrypt_file()
