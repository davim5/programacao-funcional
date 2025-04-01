
import unittest
from src.Atividade_Prog_Funcional import calcular_area

class TestFuncoesGeometria(unittest.TestCase):

    # Caso de Teste 01 - Cálculo de Potências e Raízes
    def test_area_retangulo(self):
        resultado = calcular_area('retangulo', 10, 3)
        self.assertEqual(resultado, 30)

    def test_area_triangulo(self):
        resultado = calcular_area('triangulo',15, 4)
        self.assertEqual(resultado, 30)

    def test_area_circulo(self):
        resultado = calcular_area('circulo',10)
        self.assertEqual(resultado, 314)

if __name__ == '__main__':
    unittest.main()
