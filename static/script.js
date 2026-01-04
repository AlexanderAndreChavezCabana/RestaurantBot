const BASE_URL = '/api';

const chatBox = document.getElementById('chatBox');
const inputMensaje = document.getElementById('inputMensaje');
const formChat = document.getElementById('formChat');
const btnInfo = document.getElementById('btnInfo');
const btnReiniciar = document.getElementById('btnReiniciar');
const modalInfo = document.getElementById('modalInfo');
const modalStats = document.getElementById('modalStats');

let conversacionTerminada = false;

document.addEventListener('DOMContentLoaded', async () => {
    await cargarBienvenida();
    
    formChat.addEventListener('submit', enviarMensaje);
    btnInfo.addEventListener('click', mostrarInfo);
    btnReiniciar.addEventListener('click', reiniciarBot);
    
    document.querySelectorAll('.close').forEach(btn => {
        btn.addEventListener('click', cerrarModal);
    });
    
    window.addEventListener('click', (e) => {
        if (e.target === modalInfo) modalInfo.classList.remove('show');
        if (e.target === modalStats) modalStats.classList.remove('show');
    });
    
    inputMensaje.focus();
});

async function cargarBienvenida() {
    try {
        const response = await fetch(`${BASE_URL}/inicio`);
        const data = await response.json();
        agregarMensajeBot(data.bienvenida);
    } catch (error) {
        agregarMensajeBot('¡Hola! Bienvenido a RestaurantBot. 🍽️');
    }
}

async function enviarMensaje(e) {
    e.preventDefault();
    
    const texto = inputMensaje.value.trim();
    if (!texto) return;
    
    if (conversacionTerminada) {
        alert('⚠️ La conversación ha terminado. Haz clic en "Reiniciar" para comenzar de nuevo.');
        return;
    }
    
    agregarMensajeUsuario(texto);
    inputMensaje.value = '';
    inputMensaje.focus();
    mostrarCarga();
    
    try {
        const response = await fetch(`${BASE_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ texto })
        });
        
        if (!response.ok) {
            throw new Error(`Error ${response.status}`);
        }
        
        const data = await response.json();
        removerCarga();
        agregarMensajeBot(data.respuesta);
        
        if (data.debe_terminar) {
            conversacionTerminada = true;
            inputMensaje.disabled = true;
            inputMensaje.placeholder = 'Conversación terminada. Haz clic en "Reiniciar"...';
            deshabilitarBoton();
        }
        
        scrollAlFinal();
    } catch (error) {
        removerCarga();
        agregarMensajeBot('❌ Error: No pude procesar tu mensaje. Intenta de nuevo.');
        inputMensaje.focus();
    }
}

function agregarMensajeUsuario(texto) {
    const div = document.createElement('div');
    div.className = 'mensaje usuario';
    div.innerHTML = `
        <div>
            <div class="mensaje-contenido">${escapeHtml(texto)}</div>
            <div class="mensaje-timestamp">${obtenerHora()}</div>
        </div>
    `;
    chatBox.appendChild(div);
    scrollAlFinal();
}

function agregarMensajeBot(texto) {
    const div = document.createElement('div');
    div.className = 'mensaje bot';
    const textoFormateado = escapeHtml(texto).replace(/\n/g, '<br>');
    
    div.innerHTML = `
        <div>
            <div class="mensaje-contenido">${textoFormateado}</div>
            <div class="mensaje-timestamp">${obtenerHora()}</div>
        </div>
    `;
    chatBox.appendChild(div);
    scrollAlFinal();
}

function mostrarCarga() {
    const div = document.createElement('div');
    div.className = 'mensaje bot';
    div.id = 'indicador-carga';
    div.innerHTML = `
        <div>
            <div class="mensaje-contenido">
                <div class="loading">
                    <span class="loading-dot"></span>
                    <span class="loading-dot"></span>
                    <span class="loading-dot"></span>
                </div>
            </div>
        </div>
    `;
    chatBox.appendChild(div);
    scrollAlFinal();
}

function removerCarga() {
    const indicador = document.getElementById('indicador-carga');
    if (indicador) indicador.remove();
}

function obtenerHora() {
    const ahora = new Date();
    return ahora.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' });
}

function escapeHtml(texto) {
    const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
    return texto.replace(/[&<>"']/g, m => map[m]);
}

function scrollAlFinal() {
    setTimeout(() => { chatBox.scrollTop = chatBox.scrollHeight; }, 100);
}

async function mostrarInfo() {
    modalInfo.classList.add('show');
    try {
        const response = await fetch(`${BASE_URL}/info`);
        const data = await response.json();
        
        const contenido = document.getElementById('infoContent');
        let html = `
            <div class="info-content">
                <div class="stats-item">
                    <div class="stats-label">🏪 Restaurante:</div>
                    <div class="stats-value">${data.nombre}</div>
                </div>
                <div class="stats-item">
                    <div class="stats-label">🕐 Horarios:</div>
                    <div class="stats-value">${data.horarios || 'No disponible'}</div>
                </div>
                <div class="stats-item">
                    <div class="stats-label">📍 Ubicación:</div>
                    <div class="stats-value">${data.ubicacion || 'No disponible'}</div>
                </div>
            </div>
        `;
        contenido.innerHTML = html;
    } catch (error) {
        document.getElementById('infoContent').innerHTML = '❌ Error al cargar información.';
    }
}

async function reiniciarBot() {
    if (confirm('¿Estás seguro de que deseas reiniciar la conversación?')) {
        chatBox.innerHTML = '';
        conversacionTerminada = false;
        inputMensaje.disabled = false;
        inputMensaje.placeholder = 'Escribe tu mensaje aquí...';
        habilitarBoton();
        await cargarBienvenida();
        inputMensaje.focus();
    }
}

function cerrarModal(e) {
    const modal = e.target.closest('.modal');
    if (modal) modal.classList.remove('show');
}

function deshabilitarBoton() {
    document.querySelector('.btn-enviar').disabled = true;
}

function habilitarBoton() {
    document.querySelector('.btn-enviar').disabled = false;
}

document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'r') {
        e.preventDefault();
        reiniciarBot();
    }
    if (e.ctrlKey && e.key === 'i') {
        e.preventDefault();
        mostrarInfo();
    }
});
