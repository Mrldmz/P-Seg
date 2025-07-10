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

Se continúa el desarrollo del keylogger, pero al intentar ejecutarlo en la máquina Lubuntu, se presentan problemas de compatibilidad y ejecución. Debido a estas dificultades, se decide optar por ejecutar el keylogger en un entorno Windows, aunque esto implica un menor rendimiento en cuanto a evasión de detección por software antimalware.

#### Trabajo realizado para compatibilidad con Windows

- Se revisa y adapta el código del keylogger para asegurar su correcto funcionamiento en Windows.
- Se realizan pruebas de ejecución en diferentes versiones de Windows.
- Se guarda captura del resultado según VirusTotal en `vt-klv1win-1.png`.
- Evidencia de funcionamiento en `evidencia-func-klv1win.png`.
