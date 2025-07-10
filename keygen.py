#!/usr/bin/env python3
"""
Generador de llaves RSA para el keylogger
Genera un par de llaves asimétricas y las guarda en el directorio keypair/
"""
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_keypair(key_size=2048):
    """Genera un par de llaves RSA y las guarda en archivos"""
    
    # Crear directorio keypair si no existe
    os.makedirs("keypair", exist_ok=True)
    
    # Generar llave privada
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )
    
    # Obtener llave pública
    public_key = private_key.public_key()
    
    # Rutas de archivos
    private_key_path = os.path.join("keypair", "keylogger_private.pem")
    public_key_path = os.path.join("keypair", "keylogger_public.pem")
    
    # Guardar llave privada
    with open(private_key_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    # Guardar llave pública
    with open(public_key_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    
    print(f"Llaves generadas: {private_key_path}, {public_key_path}")
    
    return private_key_path, public_key_path

def main():
    """Función principal"""
    try:
        private_path, public_path = generate_rsa_keypair(2048)
        
    except Exception as e:
        print(f"Error generando llaves: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
