import Libcplx as lc
import unittest

class TestCplxOperations(unittest.TestCase):
    #PRUEBAS SUMA DE NUMEROS COMPLEJOS
    def test_cplxsum(self):
        suma= lc.sumaC((3,2.8),(1.5,-2))
        self.assertAlmostEqual(suma[0], 4.5)
        self.assertAlmostEqual(suma[1], 0.8)
        
    def test_cplxsum2(self):
        suma= lc.sumaC((3,7),(5,2))
        self.assertAlmostEqual(suma[0], 8)
        self.assertAlmostEqual(suma[1], 9)

    #PRUEBAS MULTIPLICACION DE NUMEROS COMPLEJOS
    def test_cplxmult(self):
        mult= lc.multC((3,2.8),(1.5,-2))
        self.assertAlmostEqual(mult[0], 10.1)
        self.assertAlmostEqual(mult[1], -1.8)
    
    def test_cplxmult2(self):
        mult= lc.multC((3,7),(5,2))
        self.assertAlmostEqual(mult[0], 1)
        self.assertAlmostEqual(mult[1], 41)
    
    #PRUEBAS DIVISION DE NUMEROS COMPLEJOS
    def test_cplxdiv(self):
        div= lc.divC((3,2.8),(1.5,-2))
        self.assertAlmostEqual(div[0], -0.2)
        self.assertAlmostEqual(div[1], 1.6)
    
    def test_cplxdiv2(self):
        div= lc.divC((3,7),(5,2))
        self.assertAlmostEqual(div[0], 1)
        self.assertAlmostEqual(div[1], 1)
    
    #PRUEBAS RESTA DE NUMEROS COMPLEJOS
    def test_cplxresta(self):
        resta= lc.restaC((3,2.8),(1.5,-2))
        self.assertAlmostEqual(resta[0], 1.5)
        self.assertAlmostEqual(resta[1], 4.8)
    
    def test_cplxresta2(self):
        resta= lc.restaC((3,7),(5,2))
        self.assertAlmostEqual(resta[0], -2)
        self.assertAlmostEqual(resta[1], 5)
    
    #PRUEBAS MODULO DE UN NUMERO COMPLEJO
    def test_cplxmodulo(self):
        modulo= lc.moduloC(4,3)
        self.assertAlmostEqual(modulo, 5)
    
    def test_cplxmodulo2(self):
        modulo= lc.moduloC(5,2)
        self.assertAlmostEqual(modulo, 5.4)
    
    #PRUEBAS CONJUGADO DE UN NUMERO COMPLEJO
    def test_clpxconjugado(self):
        conj=lc.conjugadoC(4,3)
        self.assertAlmostEqual(conj[0], 4)
        self.assertAlmostEqual(conj[1], -3)
    
    def test_clpxconjugado2(self):
        conj=lc.conjugadoC(5,-2)
        self.assertAlmostEqual(conj[0], 5)
        self.assertAlmostEqual(conj[1], 2)
    
    #PRUEBAS VALORES CARTESIANOS A POLARES
    def test_clpxpolar(self):
        polar=lc.polarC(4,3)
        self.assertAlmostEqual(polar[0], 5)
        self.assertAlmostEqual(polar[1], 0.6)
    
    def test_clpxpolar2(self):
        polar=lc.polarC(5,2)
        self.assertAlmostEqual(polar[0], 5.3851648071)
        self.assertAlmostEqual(polar[1], 0.4)
     
    #PRUEBAS VALORES POLARES A CARTESIANOS
    def test_clpxcartesiana(self):
        cart=lc.cartesianoC(5,0.644)
        self.assertAlmostEqual(cart[0], 4)
        self.assertAlmostEqual(cart[1], 3)
    
    def test_clpxcartesiana2(self):
        cart=lc.cartesianoC(5.3851648071,0.4)
        self.assertAlmostEqual(cart[0], 5)
        self.assertAlmostEqual(cart[1], 2)
    
    #PRUEBAS DE LA FASE DE UN NUMERO COMPLEJO
    def test_clpxfase(self):
        fase=lc.faseC(4,3)
        self.assertAlmostEqual(fase, 0.6435011)
    
    def test_clpxfase2(self):
        fase=lc.faseC(5,2)
        self.assertAlmostEqual(fase, 0.3805063771)

if __name__ == '__main__':
    unittest.main()

