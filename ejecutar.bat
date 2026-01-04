@echo off
REM Inicia RestaurantBot con FastAPI
REM Script para Windows

echo.
echo ====================================
echo   RestaurantBot - FastAPI
echo ====================================
echo.

REM Verificar si existe el entorno virtual
if not exist "venv\" (
    echo Creando entorno virtual...
    python -m venv venv
    echo.
)

REM Activar entorno virtual
echo Activando entorno virtual...
call venv\Scripts\activate.bat
echo.

REM Verificar si están instaladas las dependencias
pip show fastapi >nul 2>&1
if errorlevel 1 (
    echo Instalando dependencias...
    pip install -r requirements.txt
    echo.
)

REM Iniciar la aplicación
echo.
echo ====================================
echo   Iniciando RestaurantBot...
echo ====================================
echo.
echo URL:           http://localhost:8000
echo Documentación: http://localhost:8000/docs
echo.
echo Presiona Ctrl+C para detener
echo.

python main.py
