# Bitácora de desarrollo

Se crea una máquina objetivo con iso de Lubuntu, llamada P2Objetivo, con dirección IP: 10.0.2.9.

## Ejercicio 1: Desarrollo de Keylogger

Se crea un keylogger básico en Python.

Se crea el ejecutable para Linux

---
### Detalles de creación de ejecutable Linux usando Docker

Se identifica que el ejecutable .exe no funcionará en Linux (Lubuntu). Se decide usar Docker para compilar un ejecutable Linux desde Windows.

Se crea un Dockerfile con las siguientes características:
- Imagen base: `python:3.11-slim`
- Instalación de dependencias del sistema para pynput
- Instalación de pynput y pyinstaller
- Compilación del keylogger a ejecutable Linux

Se construye la imagen Docker:
```ps
docker build -t keylogger-builder .
```

Se extrae el ejecutable Linux del contenedor:
```ps
docker run --rm -v "${PWD}/linux-output:/output" keylogger-builder cp /app/dist/keylogger /output/
```

---

Se continúa el desarrollo del keylogger, pero al intentar ejecutarlo en la máquina Lubuntu, se presentan problemas de compatibilidad y ejecución. Debido a estas dificultades, se decide optar por ejecutar el keylogger en un entorno Windows, aunque esto implica un menor rendimiento en cuanto a evasión de detección por software antimalware.

Para crear un ejecutable EXE en Windows se usa:
```ps
pyinstaller --onefile --noconsole --name=keylogger keylogger.py
```

#### Trabajo realizado para compatibilidad con Windows

- Se revisa y adapta el código del keylogger para asegurar su correcto funcionamiento en Windows.
- Se realizan pruebas de ejecución en diferentes versiones de Windows.
- Se guarda captura del resultado según VirusTotal en `vt-klv1win-1.png`.
- Evidencia de funcionamiento en `evidencia-func-klv1win.png`.

---

## Ejercicio 2: Cifrado y Transmisión de Datos

Se selecciona RSA como algoritmo de cifrado para los datos del keylogger.

**Ventajas**:
- Permite el intercambio seguro de datos sin necesidad de compartir una clave secreta previamente (ventaja sobre cifrado simétrico).
- RSA es ampliamente soportado y considerado seguro cuando se usan claves suficientemente largas.
- RSA es ampliamente utilizado y soportado en la mayoría de bibliotecas y herramientas criptográficas; es bueno conocerlo.
- La infraestructura de clave pública (PKI) basada en RSA está bien establecida y documentada.

Se crea `keygen.py` para generar el par de llaves asimétricas RSA-2048.

Se ejecuta exitosamente generando `keypair/keylogger_private.pem` y `keypair/keylogger_public.pem`.

### Cifrado

Se desarrolla `encrypt-simple.py` para implementar el cifrado RSA de los datos capturados por el keylogger.

**Características del script**:
- Carga la clave pública RSA desde `keypair/keylogger_public.pem`
- Lee los datos del archivo de log del keylogger
- Cifra el contenido usando RSA con padding OAEP
- Guarda los datos cifrados en un archivo binario

### Descifrado

