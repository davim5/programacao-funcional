
import unittest
from src.Atividade_Prog_Funcional import calcular_area, calcular_areas_multiplas, calcular_area_com_escala, calcular_hipotenusa

class TestFuncoesGeometria(unittest.TestCase):

    # Caso de Teste 01 - Cáculo área do retângulo
    def test_area_retangulo(self):
        resultado = calcular_area('retangulo', 10, 3)
        self.assertEqual(resultado, 30)

    # Caso de Teste 02 - Cáculo área do retângulo
    def test_area_triangulo(self):
        resultado = calcular_area('triangulo',15, 4)
        self.assertEqual(resultado, 30)

    # Caso de Teste 03 - Cáculo área do círculo
    def test_area_circulo(self):
        resultado = calcular_area('circulo',10)
        self.assertEqual(resultado, 314.15927)
        
    # Caso de Teste 04 - Cálculo de múltiplas áreas
    def test_calcular_areas_multiplas(self):
        formas = [
            ('circulo', (10,)),
            ('retangulo', (5, 6)),
            ('triangulo', (8, 4))
        ]
        resultado = calcular_areas_multiplas(formas)
        self.assertEqual(resultado, [314.15927, 30, 16]) 

    # Caso de Teste 05 - Cálculo de área com fator de escala
    def test_calcular_area_com_escala(self):
        resultado = calcular_area_com_escala(calcular_area, 'retangulo', 2, 10, 5)
        self.assertEqual(resultado, 100)

    # Caso de Teste 06 - Cálculo da hipotenusa
    def test_calcular_hipotenusa(self):
        hipotenusa_func = calcular_hipotenusa(3, 4)
        resultado = hipotenusa_func()
        self.assertEqual(resultado, 5.0)
if __name__ == '__main__':
    unittest.main()
