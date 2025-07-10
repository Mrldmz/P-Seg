@echo off
echo Iniciando servidor keylogger...
echo.

cd /d "%~dp0"

if not exist "data" mkdir data
if not exist "logs" mkdir logs
if not exist "data\encrypted" mkdir data\encrypted
if not exist "data\decrypted" mkdir data\decrypted

docker-compose up -d

if %errorlevel% equ 0 (
    echo.
    echo Servidor iniciado correctamente
    echo Puerto: http://localhost:5000
    echo Logs: docker-compose logs -f
) else (
    echo.
    echo Error al iniciar el servidor
    pause
)

pause
