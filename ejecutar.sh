#!/bin/bash
# Inicia RestaurantBot con FastAPI
# Script para Mac/Linux

echo ""
echo "===================================="
echo "  RestaurantBot - FastAPI"
echo "===================================="
echo ""

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
    echo ""
fi

# Activar entorno virtual
echo "Activando entorno virtual..."
source venv/bin/activate
echo ""

# Instalar dependencias si es necesario
pip show fastapi > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Instalando dependencias..."
    pip install -r requirements.txt
    echo ""
fi

# Iniciar la aplicación
echo ""
echo "===================================="
echo "  Iniciando RestaurantBot..."
echo "===================================="
echo ""
echo "URL:           http://localhost:8000"
echo "Documentación: http://localhost:8000/docs"
echo ""
echo "Presiona Ctrl+C para detener"
echo ""

python main.py
