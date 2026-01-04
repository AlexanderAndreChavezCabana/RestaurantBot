# Guía de Inicio Rápido - RestaurantBot con FastAPI

## 🚀 Instalación y Ejecución

### 1️⃣ Crear Entorno Virtual

```bash
# Navegar a la carpeta
cd RestaurantBot

# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Activar entorno (Mac/Linux)
source venv/bin/activate
```

### 2️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la API

```bash
python main.py
```

O alternativamente:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4️⃣ Acceder a la Interfaz

Abre tu navegador en:

```
http://localhost:8000
```

📚 **Documentación interactiva (Swagger UI)**:
```
http://localhost:8000/docs
```

## 📡 Endpoints de la API

### Chat
- `GET /api/inicio` - Obtiene bienvenida
- `POST /api/chat` - Envía mensaje y obtiene respuesta
- `GET /api/historial` - Obtiene historial completo
- `GET /api/estadisticas` - Obtiene estadísticas

### Información
- `GET /api/menu` - Información del menú
- `GET /api/info` - Información del restaurante
- `GET /api/config` - Configuración del bot

### Control
- `POST /api/reiniciar` - Reinicia la conversación
- `GET /health` - Verifica salud de la API

## 🎨 Interfaz Web

La interfaz incluye:
- ✅ Chat en tiempo real
- ✅ Diseño responsive (móvil, tablet, desktop)
- ✅ Modal de información del restaurante
- ✅ Botón de reinicio
- ✅ Indicadores de carga
- ✅ Timestamps en mensajes
- ✅ Soporte para emojis

## 📦 Estructura de Carpetas

```
RestaurantBot/
├── main.py                     # Aplicación FastAPI
├── restaurant_bot.py           # Lógica del chatbot
├── flujos_restaurante.json     # Flujos de conversación
├── test_restaurant_bot.py      # Tests
├── requirements.txt            # Dependencias
├── .gitignore                  # Archivos a ignorar
├── README.md                   # Documentación
├── INICIO_RAPIDO.md           # Este archivo
└── static/
    ├── index.html              # Página principal
    ├── style.css               # Estilos CSS
    └── script.js               # Lógica JavaScript
```

## 🧪 Ejecutar Tests

```bash
# Con unittest
python test_restaurant_bot.py

# O con unittest -m
python -m unittest test_restaurant_bot -v
```

## 🔧 Solución de Problemas

### Puerto 8000 en uso

```bash
# Usar otro puerto
uvicorn main:app --reload --port 8001
```

### Caracteres especiales no se muestran

```bash
# En Windows PowerShell
chcp 65001
python main.py
```

### Módulos no encontrados

```bash
# Asegurar que el entorno virtual está activado
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Luego instalar dependencias
pip install -r requirements.txt
```

## 💡 Características de la UI

### Atajos de Teclado
- `Ctrl+R` - Reiniciar conversación
- `Ctrl+I` - Mostrar información
- `Enter` - Enviar mensaje

### Ejemplos de Conversación

```
Usuario: Hola
Bot: ¡Hola! Bienvenido a RestauBOT...

Usuario: Quiero una pizza
Bot: Nuestras pizzas son artesanales...

Usuario: Cuál es el horario
Bot: HORARIOS DE ATENCIÓN...

Usuario: Hacer una reserva
Bot: Perfecto! Vamos a hacer tu reserva...

Usuario: Adiós
Bot: ¡Gracias por visitarnos!
```

## 📊 API Response Example

### POST /api/chat
```json
{
  "respuesta": "¡Hola! Bienvenido a RestauBOT 🍽️",
  "debe_terminar": false,
  "historial": [
    {
      "usuario": "hola"
    },
    {
      "bot": "¡Hola! Bienvenido..."
    }
  ],
  "estadisticas": {
    "total_mensajes": 2,
    "flujo_actual": "flujo_menu_pedidos",
    "ultima_intencion": "saludo"
  }
}
```

## 🚀 Deploy en Producción

Para desplegar en producción:

```bash
# Usar Gunicorn (servidor WSGI robusto)
pip install gunicorn

# Ejecutar con Gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

## 📝 Notas

- El chatbot mantiene el contexto durante la sesión
- Los flujos se cargan desde JSON (fácil de editar)
- La API es RESTful y JSON-based
- La interfaz es completamente responsive
- Soporta múltiples sesiones simultáneas

## 🎓 Conceptos Aprendidos

- FastAPI y creación de APIs REST
- Servicio de archivos estáticos con FastAPI
- Comunicación cliente-servidor con Fetch API
- Diseño responsive con CSS Grid/Flexbox
- Manejo de estados en JavaScript
- Documentación automática con Swagger

---

**¡Listo para usar!** Disfruta tu RestaurantBot 🍽️
