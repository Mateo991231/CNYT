import unittest
import complex

class TestStringMethods(unittest.TestCase):
    ##
    def test_deberiaSumarNumerosComplejos(self):
        self.assertEquals(complex.suma(10,8,7,6),("18+13i"))

if __name__=='__main__':
    unittest.main()
