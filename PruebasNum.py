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
    def test_deberiaSumarVector(self):
       self.assertEqual(complexCal.sumaVector(([(2,3),(3,2)]),([(2,5),(3,2)])),[(4, 8), (6, 4)])
    def test_deberiaMultiplicarEscalar(self):
        self.assertEqual(complexCal. productoVectorEscalar((5,3),([(2,5),(3,2)])),[(-5, 31), (9, 19)])
    def test_deberiaHacerProductoTensor(self):
        self.assertEqual(complexCal.productoTensor(([(2,3),(3,2)]),([(2,5),(3,2)])),[[(-11, 16), (0, 13)], [(-4, 19), (5, 12)]])
    def test_deberiaHacerInversoVector(self):
        self.assertEqual(complexCal.inversoVector(([(2,3),(3,2)])),[(-2, -3), (-3, -2)])
    def test_deberiaHacerInversoMatriz(self):
        self.assertEqual(complexCal.inversaMatriz(([[(2,2),(3,3)],[(2,2),(3,3)]])),[[(-2, -2), (-3, -3)], [(-2, -2), (-3, -3)]])
    def test_deberiaHacersumaMat (self):
        a=([[(2,5),(8,3)],[(1,2),(4,3)]])
        b=([[(2,2),(3,3)],[(2,2),(3,3)]])
        self.assertEqual(complexCal.sumaMatrices(a,b),[[(4, 7), (11, 6)], [(3, 4), (7, 6)]])
    def test_deberiaHacerProductoInternovec(self):
        a=([(2,3),(3,2)])
        b=([(2,3),(3,2)])
        self.assertEqual(complexCal.productoInternoVec (a,b), (0, 24))
    def test_deberiaHacerTranspuesta(self):
        a=([[(2,5),(8,3)],[(1,2),(4,3)]])
        self.assertEqual(complexCal.transpuesta (a), [[(2, 5), (1, 2)], [(8, 3), (4, 3)]])
    def test_deberiaHacerConjugada(self):
        a=([[(2,5),(8,3)],[(1,2),(4,3)]])
        self.assertEqual(complexCal.conjugada (a), [[(2, 5), (8, 3)], [(1, 2), (4, 3)]] )
        
    def test_deberiaHacerAdjunta(self):
        a=([[(2,5),(8,3)],[(1,2),(4,3)]])
        self.assertEqual(complexCal.adjunta(a), [[(2, 5), (1, 2)], [(8, 3), (4, 3)]] )
    
    def test_deberiaMultiMatriz(self):
        a=([(2,3),(3,2)])
        b=([(2,3),(3,2)])
        self.assertEqual(complexCal.multiMat(a,b), (0, 24))


         
if __name__=="__main__":
    unittest.main()

