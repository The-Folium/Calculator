import unittest
from expression import Expression

class Expression_testCase(unittest.TestCase):

    def test01(self):
        self.assertEqual(Expression("2+3").evaluate(), "5")

    def test02(self):
        self.assertEqual(Expression("pi").evaluate(), "3.14159265359")

    def test03(self):
        self.assertEqual(Expression("pi**2").evaluate(), "9.869604401089")

    def test04(self):
        self.assertEqual(Expression("3+0.4*(5-12*(3-0.545*3))").evaluate(), "-1.552")

    def test05(self):
        self.assertEqual(Expression("sin(pi/6)").evaluate(), "0.5")

    def test06(self):
        self.assertEqual(Expression("sin(0.6)**2+cos(0.6)**2").evaluate(), "1.0")

    def test07(self):
        self.assertEqual(Expression("log(100)").evaluate(), "2.0")

    def test08(self):
        self.assertEqual(Expression("asin(0.5)-pi/6").evaluate(), "0.0")

    def test09(self):
        self.assertEqual(Expression("sqrt(2)").evaluate(), "1.414213562373")

    def test10(self):
        self.assertEqual(Expression("sqrt(1-(sin(pi/3))**2)").evaluate(), "0.5")


if __name__ == '__main__':
    unittest.main()
