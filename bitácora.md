Se crea una máquina objetivo con iso de Lubuntu, llamada P2Objetivo, con dirección IP: 10.0.2.9.

Se crea un keylogger básico en Python.

Para crear un ejecutable EXE en Windows se usa:
```ps
pyinstaller --onefile --noconsole --name=keylogger keylogger.py
```

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
