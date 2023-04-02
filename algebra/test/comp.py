import unittest

class Algebra_tests(unittest.TestCase):
    term = None

    def test_term_division(self):
        t1 = self.term('2x2')
        t2 = self.term('2x')
        self.assertEqual(t2/t1,self.term('xᐨ¹'))
        self.assertRaises(TypeError,lambda:t1/'r')
    
    def test_polynom_division(self):
        term = self.term
        pol1 = term('2x') + term('3y')
        self.assertEqual(str(pol1/term('2x')),'1 + 1.5xᐨ¹y')
        self.assertEqual(pol1/pol1,1)


    def test_comp(self):
        term = self.term
        pol1 = term('2x') + term('3y')
        self.assertEqual(pol1.plot(univ=1),5)

    def test_complex(self):
        term = self.term
        t1 = term('2x2+1jy2+3j')
        t2 = term('4x4+2jy4+6j')
        t3 = term('2+1jx3+4j')
        self.assertEqual(str(t1),'2x²⁺¹ⁱy²⁺³ⁱ')
        self.assertEqual(term(str(t3)),t3)


    def test_complex_mul(self):
        term = self.term
        t1 = term('2x2+1jy2+3j')
        t2 = term('4x4+2jy4+6j') 
        self.assertEqual(t1*t2,t1**3)
        self.assertEqual(t1*complex(2,1),term('4+2jx2+1jy2+3j'))
        self.assertEqual(str(t1*(2+1j)),str(term('4+2jx2+1jy2+3j')))
    
    def test_complex_division(self):
        term = self.term
        t1 = term('2x2+1jy2+3j')
        t2 = term('4x4+2jy4+6j')
        self.assertEqual(t2/t1,t1)
        self.assertEqual(t1/t2,t1**-1)

    def test_complex_powers(self):
        term = self.term
        t1 = term('2x2+1jy2+3j')
        t2 = term('4x4+2jy4+6j')
        self.assertEqual(t1**-0.25,term(str(t1**-0.25)))
        self.assertEqual(t1**2,t2)




    def test_degree(self):
        term = self.term
        t1 = term('2x')   
        t2 = term('2x2')
        self.assertEqual(t1.degree(),1)
        self.assertEqual(t2.degree(),2)
        self.assertEqual((t1+t2).degree(),2)
        self.assertEqual((t1**(2+1j)).degree(),2+1j)

 
        

        


        
    



        