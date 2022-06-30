import unittest

class Algebra_tests(unittest.TestCase):
    term = None
    def test_term_division(self):
        t1 = self.term('2x2')
        t2 = self.term('2x')
        self.assertEqual(t2/t1,self.term('xᐨ¹'))
    
    def test_polynom_division(self):
        term = self.term
        pol1 = term('2x') + term('3y')
        self.assertEqual(str(pol1/term('2x')),'1 + 1.5xᐨ¹y')

    def test_comp(self):
        term = self.term
        pol1 = term('2x') + term('3y')
        self.assertEqual(pol1.plot(univ=1),5)


        
    



        