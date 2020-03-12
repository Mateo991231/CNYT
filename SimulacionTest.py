import unittest,complexCal
class TestCases(unittest.TestCase):
    def test_probabilidad(self):
        self.assertEqual(complexCal.proba(2,[(7,5),(2,3),(1,2)]),15.48100641346688)
    def test_transicion(self):
        self.assertEqual(complexCal.ampli(a=[(7,5),(5,2),(4,2)]
                                          [(7,5),(2,3),(1,2)]),(98.0, -17.0))
    
if __name__=="__main__":
    unittest.main()
