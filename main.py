#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
from pathlib import Path
from restaurant_bot import RestaurantBot

class MensajeUsuario(BaseModel):
    texto: str

class RespuestaBot(BaseModel):
    respuesta: str
    debe_terminar: bool
    historial: list = []
    estadisticas: dict = {}

class InicioBot(BaseModel):
    bienvenida: str
    flujos: list

app = FastAPI(
    title="RestaurantBot API",
    description="Chatbot inteligente para restaurante",
    version="1.0.0"
)

bot_instance = RestaurantBot('flujos_restaurante.json')

ruta_static = Path(__file__).parent / "static"
if ruta_static.exists():
    app.mount("/static", StaticFiles(directory=str(ruta_static)), name="static")

@app.get("/")
async def raiz():
    ruta_html = Path(__file__).parent / "static" / "index.html"
    if ruta_html.exists():
        return FileResponse(str(ruta_html))
    return {"mensaje": "RestaurantBot API"}

@app.get("/api/inicio", response_model=InicioBot)
async def obtener_inicio():
    flujos = list(bot_instance.flujos.keys())
    nombres_flujos = [bot_instance.flujos[f].get('nombre', f) for f in flujos]
    return InicioBot(bienvenida=bot_instance.config['mensaje_bienvenida'], flujos=nombres_flujos)

@app.post("/api/chat", response_model=RespuestaBot)
async def procesar_mensaje(mensaje: MensajeUsuario):
    if not mensaje.texto or not mensaje.texto.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")
    
    try:
        respuesta, debe_terminar = bot_instance.procesar_entrada(mensaje.texto)
        historial = bot_instance.obtener_historial()
        estadisticas = bot_instance.obtener_estadisticas()
        
        return RespuestaBot(
            respuesta=respuesta,
            debe_terminar=debe_terminar,
            historial=historial,
            estadisticas=estadisticas
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/api/historial")
async def obtener_historial():
    return {
        "historial": bot_instance.obtener_historial(),
        "total_mensajes": len(bot_instance.obtener_historial())
    }

@app.get("/api/estadisticas")
async def obtener_estadisticas():
    stats = bot_instance.obtener_estadisticas()
    flujos = list(bot_instance.flujos.keys())
    return {
        **stats,
        "flujos_disponibles": flujos,
        "nombre_restaurante": bot_instance.config['nombre_restaurante']
    }

@app.get("/api/menu")
async def obtener_menu():
    try:
        ruta_flujos = Path(__file__).parent / "flujos_restaurante.json"
        with open(ruta_flujos, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        flujo_menu = data['flujos']['flujo_menu_pedidos']
        for intencion in flujo_menu['intenciones']:
            if intencion['id'] == 'ver_menu':
                return {"menu_disponible": True, "descripcion": intencion['respuestas'][0]}
        
        return {"menu_disponible": False}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/api/info")
async def obtener_info():
    config = bot_instance.config
    flujos = bot_instance.flujos
    
    info_horarios = None
    info_ubicacion = None
    
    for intencion in flujos['flujo_informacion_restaurante']['intenciones']:
        if intencion['id'] == 'consultar_horario':
            info_horarios = intencion['respuestas'][0]
        elif intencion['id'] == 'consultar_ubicacion':
            info_ubicacion = intencion['respuestas'][0]
    
    return {
        "nombre": config['nombre_restaurante'],
        "horarios": info_horarios,
        "ubicacion": info_ubicacion,
        "umbral_similitud": config['umbral_similitud']
    }

@app.post("/api/reiniciar")
async def reiniciar_bot():
    global bot_instance
    bot_instance = RestaurantBot('flujos_restaurante.json')
    return {
        "estado": "reiniciado",
        "mensaje": "El chatbot ha sido reiniciado",
        "bienvenida": bot_instance.config['mensaje_bienvenida']
    }

@app.get("/api/config")
async def obtener_configuracion():
    return {
        "nombre_restaurante": bot_instance.config['nombre_restaurante'],
        "umbral_similitud": bot_instance.config['umbral_similitud'],
        "mensaje_bienvenida": bot_instance.config['mensaje_bienvenida'],
        "mensaje_despedida": bot_instance.config['mensaje_despedida'],
        "flujos_disponibles": list(bot_instance.flujos.keys())
    }

@app.get("/health")
async def health_check():
    return {"status": "ok", "servicio": "RestaurantBot API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    print("🚀 Iniciando RestaurantBot API...")
    print("📍 URL: http://localhost:8000")
    print("📚 Documentación: http://localhost:8000/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
