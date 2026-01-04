import json
import re
import difflib
import random
import unicodedata
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass


class RestaurantBot:

    def __init__(self, archivo_flujos='flujos_restaurante.json'):
        self.archivo_flujos = archivo_flujos
        self.cargar_flujos()
        self.contexto = {
            'nombre_usuario': None,
            'flujo_actual': None,
            'ultima_intencion': None,
            'historial': [],
            'pedido_actual': [],
            'reserva_actual': {}
        }

    def cargar_flujos(self):
        try:
            ruta = Path(__file__).parent / self.archivo_flujos
            with open(ruta, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.config = data['configuracion']
            self.flujos = data['flujos']
            print("Flujos de conversación cargados correctamente\n")

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.archivo_flujos}")
            exit(1)
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.archivo_flujos} no es un JSON válido")
            exit(1)

    def normalizar_texto(self, texto):
        texto = texto.lower()
        texto = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
        texto = re.sub(r'[^\w\s]', '', texto)
        texto = ' '.join(texto.split())
        return texto

    def calcular_similitud(self, texto1, texto2):
        return difflib.SequenceMatcher(None, texto1, texto2).ratio()

    def encontrar_intencion(self, texto_usuario):
        texto_normalizado = self.normalizar_texto(texto_usuario)
        mejor_coincidencia = None
        mejor_score = 0
        mejor_flujo = None

        for flujo_id, flujo_data in self.flujos.items():
            for intencion in flujo_data['intenciones']:
                for patron in intencion['patrones']:
                    patron_normalizado = self.normalizar_texto(patron)
                    similitud = self.calcular_similitud(
                        texto_normalizado,
                        patron_normalizado
                    )

                    if patron_normalizado in texto_normalizado:
                        similitud = min(1.0, similitud + 0.3)

                    if similitud > mejor_score:
                        mejor_score = similitud
                        mejor_coincidencia = intencion
                        mejor_flujo = flujo_id

        umbral = self.config['umbral_similitud']
        if mejor_score >= umbral:
            self.contexto['flujo_actual'] = mejor_flujo
            self.contexto['ultima_intencion'] = mejor_coincidencia['id']
            return mejor_flujo, mejor_coincidencia
        else:
            self.contexto['flujo_actual'] = None
            self.contexto['ultima_intencion'] = None
            return None, None

    def generar_respuesta(self, intencion):
        respuesta = random.choice(intencion['respuestas'])

        if 'siguiente_sugerencia' in intencion:
            respuesta += f"\n\n💡 {intencion['siguiente_sugerencia']}"

        return respuesta

    def procesar_entrada(self, texto_usuario):
        self.contexto['historial'].append({
            'usuario': texto_usuario,
            'timestamp': None
        })

        flujo_id, intencion = self.encontrar_intencion(texto_usuario)

        if intencion:
            respuesta = self.generar_respuesta(intencion)

            if 'accion_especial' in intencion:
                if intencion['accion_especial'] == 'terminar':
                    self.contexto['historial'].append({
                        'bot': respuesta,
                        'accion': 'terminar'
                    })
                    return respuesta, True

            self.contexto['historial'].append({'bot': respuesta})
            return respuesta, False

        else:
            respuesta = self.config['mensaje_no_entendido']
            self.contexto['historial'].append({'bot': respuesta})
            return respuesta, False

    def mostrar_bienvenida(self):
        print("\n" + "="*60)
        print(f"{'RestaurantBot - Tu Asistente Virtual':^60}")
        print("="*60 + "\n")
        print(self.config['mensaje_bienvenida'])
        print("\n" + "-"*60 + "\n")

    def ejecutar(self):
        self.mostrar_bienvenida()

        while True:
            try:
                entrada = input("🧑 Tú: ").strip()

                if not entrada:
                    print("⚠️ Por favor, escribe algo.\n")
                    continue

                respuesta, debe_terminar = self.procesar_entrada(entrada)

                print(f"\n🤖 RestauBot: {respuesta}\n")
                print("-"*60 + "\n")

                if debe_terminar:
                    break

            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta pronto! Gracias por visitarnos.")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}\n")

    def obtener_historial(self):
        return self.contexto['historial']

    def obtener_estadisticas(self):
        return {
            'total_mensajes': len(self.contexto['historial']),
            'flujo_actual': self.contexto['flujo_actual'],
            'ultima_intencion': self.contexto['ultima_intencion']
        }


def main():
    bot = RestaurantBot('flujos_restaurante.json')
    bot.ejecutar()


if __name__ == '__main__':
    main()
