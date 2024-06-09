import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculadora()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtrai(self):
        self.assertEqual(self.calculator.subtrai(10, 5), 5)
        self.assertEqual(self.calculator.subtrai(-1, 1), -2)
        self.assertEqual(self.calculator.subtrai(-1, -1), 0)

    def test_multiplica(self):
        self.assertEqual(self.calculator.multiplica(3, 7), 21)
        self.assertEqual(self.calculator.multiplica(-1, 1), -1)
        self.assertEqual(self.calculator.multiplica(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-1, 1), -1)
        self.assertEqual(self.calculator.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
