import unittest
import complexCal

class TestCases(unittest.TestCase):
    def test_DeberiaSumar(self):
        self.assertEqual(complexCal.suma((-3,-2),(7,-2)),(4, -4))
    def test_DeberiaRestar(self):
        self.assertEqual(complexCal.resta((-3,-2),(7,-2)),(-10,0))
    def test_Deberiamultiplicar(self):
        self.assertEqual(complexCal.multiplicacion((1,2),(-1,-3)),(5,-5))
    def test_deberiaHacerDivision(self):
        self.assertEqual(complexCal.divi((10,20),(30,5)),(0.43243243243243246,0.5945945945945946))
    def test_deberiaHacerConjugado(self):
        self.assertEqual(complexCal.conjugado((10,-5)),(10,5))
    def test_deberiaHacerModulo(self):
        self.assertEqual(complexCal.modulo((10,5)),(11.180339887498949))
    def test_deberiaPasarDePolarCartesiano(self):
        self.assertEqual(complexCal.polarCartesiano((10,5)),(9.961946980917455, 0.8715574274765816))
    def test_deberiaPasarDeCartesianopolar(self):
       self.assertEqual(complexCal.cartesianoPolar((3,4)),(9765625, 53.13010235415598))
    def test_deberiaRetornarFaseComplejo(self):
       self.assertEqual(complexCal.fase((10,5)),0.4636476090008061)
    
if __name__=="__main__":
    unittest.main()

