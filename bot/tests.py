import funciones
import unittest
class TestClash(unittest.TestCase):


	def test_parametro(self):
		#funcion para testear la funcion de extraer puntos de vida de un personaje
		self.assertEqual(funciones.extraerPuntosVida('personaje prueba'), 0)
		#self.assertEqual(funciones.extraerPuntosVida('Principe'), 0)
		#Funcion para testear que la clasificacion de personajes con mas vida es un string
		self.assertTrue(isinstance(funciones.clasificacionPersonajesVida(),str))
		#Funcion para testear que la funcion paraa extraer puntos de vida devuelve un entero
		self.assertTrue(isinstance(funciones.extraerPuntosVida("Principe"),int))

if __name__ == '__main__':
    unittest.main()

