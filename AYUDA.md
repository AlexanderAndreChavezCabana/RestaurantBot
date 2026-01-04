# RestaurantBot - Ayuda Rápida ⚡

## 🚀 Inicio en 30 segundos

```bash
# Windows
ejecutar.bat

# Mac/Linux
chmod +x ejecutar.sh
./ejecutar.sh
```

**URL:** http://localhost:8000

---

## 📞 Comandos Rápidos

| Acción | Comando |
|--------|---------|
| Instalar | `pip install -r requirements.txt` |
| Ejecutar API | `python main.py` |
| Ejecutar Tests | `python test_restaurant_bot.py` |
| Ver Docs | `http://localhost:8000/docs` |
| Crear venv | `python -m venv venv` |
| Activar venv (W) | `venv\Scripts\activate` |
| Activar venv (M/L) | `source venv/bin/activate` |

---

## 🎯 Ejemplos de Mensajes

### Menú
- "menu"
- "quiero una pizza"
- "dame una hamburguesa"
- "que pasta tienes"
- "un postre"
- "con bebida"

### Reservas
- "quiero reservar"
- "hacer una reserva"
- "mesa para 4"
- "el sábado a las 19:00"
- "cambiar mi reserva"
- "cancelar reserva"

### Información
- "horario"
- "donde estan"
- "metodos de pago"
- "promociones"
- "wifi"
- "ambiente"

### Otros
- "hola"
- "gracias"
- "adios"
- "salir"

---

## 🔗 URLs Importantes

```
Página Principal:   http://localhost:8000
Documentación:      http://localhost:8000/docs
ReDoc:              http://localhost:8000/redoc
Health Check:       http://localhost:8000/health
```

---

## 🛠️ Estructura API

### GET Requests
```
/api/inicio              → Bienvenida
/api/historial          → Historial
/api/estadisticas       → Estadísticas
/api/menu               → Menú
/api/info               → Info restaurante
/api/config             → Configuración
/health                 → Estado
```

### POST Requests
```
/api/chat               → Enviar mensaje
/api/reiniciar          → Reiniciar bot
```

---

## 📱 Respuesta JSON Ejemplo

```json
{
  "respuesta": "¡Hola! Bienvenido a RestauBOT 🍽️",
  "debe_terminar": false,
  "historial": [...],
  "estadisticas": {
    "total_mensajes": 1,
    "flujo_actual": "flujo_menu_pedidos",
    "ultima_intencion": "saludo"
  }
}
```

---

## ⌨️ Atajos de Teclado

| Atajo | Función |
|-------|---------|
| `Ctrl+R` | Reiniciar chat |
| `Ctrl+I` | Mostrar información |
| `Enter` | Enviar mensaje |

---

## 🐛 Problemas Comunes

### Puerto ocupado
```bash
uvicorn main:app --reload --port 8001
```

### ModuleNotFoundError
```bash
pip install fastapi uvicorn
```

### Caracteres extraños
```bash
chcp 65001  # Windows PowerShell
python main.py
```

### Entorno virtual no encontrado
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

---

## 📊 Flujos de Conversación

### 1. Menú & Pedidos 🍽️
- Ver menú
- Pedir pizzas, hamburguesas, pastas
- Agregar bebidas y postres
- Confirmar pedido

### 2. Reservas 📅
- Hacer nueva reserva
- Modificar detalles
- Cancelar reserva

### 3. Información ℹ️
- Horarios
- Ubicación
- Ambiente
- Pagos
- Promociones

---

## 🔧 Configuración

Editar `flujos_restaurante.json`:

```json
{
  "configuracion": {
    "umbral_similitud": 0.6,        // Sensibilidad
    "nombre_restaurante": "RestauBOT",
    "mensaje_bienvenida": "..."
  }
}
```

---

## 📈 Estadísticas

```
Archivos: 12
Código: 1500+ líneas
Endpoints: 9
Intenciones: 30+
Patrones: 100+
Tests: 15+
```

---

## 🧪 Testing Rápido

```bash
# Todos los tests
python test_restaurant_bot.py

# Tests específicos
python -m unittest test_restaurant_bot.TestRestaurantBot.test_saludo_basico -v
```

---

## 📚 Recursos

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)
- [Python Docs](https://docs.python.org/3/)

---

## ✅ Checklist Pre-Uso

- [ ] Python 3.8+ instalado
- [ ] Clonar/descargar proyecto
- [ ] Crear entorno virtual
- [ ] Instalar dependencias
- [ ] Ejecutar main.py
- [ ] Abrir http://localhost:8000
- [ ] ¡Disfrutar!

---

## 🎓 Conceptos Clave

- **Chatbot**: Programa que simula conversación
- **Intención**: Lo que el usuario quiere hacer
- **Patrón**: Texto que identifica una intención
- **Flujo**: Secuencia de intenciones relacionadas
- **API REST**: Interfaz web para consultar datos
- **FastAPI**: Framework moderno de Python
- **Swagger**: Documentación automática

---

**¡Listo para chatear! 🚀**

Para más detalles, ver:
- README.md - Documentación completa
- INICIO_RAPIDO.md - Guía detallada
- RESUMEN.md - Visión general del proyecto
