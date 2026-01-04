import unittest
from restaurant_bot import RestaurantBot


class TestRestaurantBot(unittest.TestCase):

    def setUp(self):
        self.bot = RestaurantBot('flujos_restaurante.json')

    def test_carga_flujos(self):
        self.assertIsNotNone(self.bot.flujos)
        self.assertIn('flujo_menu_pedidos', self.bot.flujos)
        self.assertIn('flujo_reservas', self.bot.flujos)
        self.assertIn('flujo_informacion_restaurante', self.bot.flujos)

    def test_normalizacion_texto(self):
        texto_original = "¡Hola! ¿Cómo estás?"
        texto_normalizado = self.bot.normalizar_texto(texto_original)
        
        self.assertEqual(texto_normalizado, texto_normalizado.lower())
        self.assertNotIn('¡', texto_normalizado)
        self.assertNotIn('¿', texto_normalizado)

    def test_similitud_textos(self):
        similitud = self.bot.calcular_similitud('hola', 'hola')
        self.assertEqual(similitud, 1.0)
        
        similitud_diferente = self.bot.calcular_similitud('hola', 'adios')
        self.assertLess(similitud_diferente, similitud)

    def test_saludo_basico(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("hola")
        
        self.assertIsNotNone(respuesta)
        self.assertFalse(debe_terminar)
        self.assertGreater(len(respuesta), 0)

    def test_menu_pizza(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("quiero una pizza")
        
        self.assertIsNotNone(respuesta)
        self.assertFalse(debe_terminar)
        self.assertIn('pizza', respuesta.lower())

    def test_hamburguesa(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("dame una hamburguesa")
        
        self.assertIsNotNone(respuesta)
        self.assertIn('hamburguesa', respuesta.lower())

    def test_reserva(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("quiero hacer una reserva")
        
        self.assertIsNotNone(respuesta)
        self.assertFalse(debe_terminar)

    def test_horarios(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("cual es el horario")
        
        self.assertIsNotNone(respuesta)
        self.assertIn('horario', respuesta.lower())

    def test_ubicacion(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("donde estan ubicados")
        
        self.assertIsNotNone(respuesta)
        self.assertIn('ubicación', respuesta.lower())

    def test_despedida(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("adios")
        
        self.assertIsNotNone(respuesta)
        self.assertTrue(debe_terminar)

    def test_entrada_invalida(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("xyzabc123")
        
        self.assertIsNotNone(respuesta)
        self.assertFalse(debe_terminar)
        self.assertIn('no entendí', respuesta.lower())

    def test_historial(self):
        self.bot.procesar_entrada("hola")
        self.bot.procesar_entrada("menu")
        
        historial = self.bot.obtener_historial()
        self.assertGreater(len(historial), 0)

    def test_estadisticas(self):
        self.bot.procesar_entrada("hola")
        estadisticas = self.bot.obtener_estadisticas()
        
        self.assertIn('total_mensajes', estadisticas)
        self.assertIn('flujo_actual', estadisticas)
        self.assertIn('ultima_intencion', estadisticas)

    def test_promociones(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("que promociones tienen")
        
        self.assertIsNotNone(respuesta)
        self.assertFalse(debe_terminar)

    def test_metodos_pago(self):
        respuesta, debe_terminar = self.bot.procesar_entrada("que metodos de pago aceptan")
        
        self.assertIsNotNone(respuesta)
        self.assertFalse(debe_terminar)


class TestRestaurantBotIntegracion(unittest.TestCase):

    def setUp(self):
        self.bot = RestaurantBot('flujos_restaurante.json')

    def test_conversacion_completa_pedido(self):
        conversacion = [
            ("hola", False),
            ("quiero ver el menu", False),
            ("dame una pizza margherita", False),
            ("con refresco", False),
            ("listo", False),
        ]

        for entrada, esperado_terminar in conversacion:
            respuesta, debe_terminar = self.bot.procesar_entrada(entrada)
            self.assertEqual(debe_terminar, esperado_terminar)
            self.assertIsNotNone(respuesta)

    def test_conversacion_completa_reserva(self):
        conversacion = [
            "hola",
            "quiero hacer una reserva",
            "somos 4 personas",
            "el sabado a las 19 horas",
        ]

        for entrada in conversacion:
            respuesta, debe_terminar = self.bot.procesar_entrada(entrada)
            self.assertIsNotNone(respuesta)
            self.assertFalse(debe_terminar)


def run_tests():
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == '__main__':
    run_tests()
