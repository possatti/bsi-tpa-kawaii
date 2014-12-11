import unittest
from cliente import Cliente

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.lucas = Cliente("Lucas", "Possatti", "Guatemala", "1234-5678", 9234)
        self.outrolucas = Cliente("Lucas", "Possatti", "Guatemala", "1234-5678", 9234)
        self.mateus = Cliente("Mateus", "Possatti", "Guatemala", "7894-4568", 2563)

    def test_eq(self):
        self.assertFalse(self.lucas is self.outrolucas)
        self.assertTrue(self.lucas == self.outrolucas)

    def test_lt(self):
        self.assertFalse(self.lucas < self.outrolucas)
        self.assertTrue(self.mateus < self.lucas)

if __name__ == '__main__':
    unittest.main()
