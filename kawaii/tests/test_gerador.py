import unittest
import os

from kawaii.gerador import *
from kawaii.cliente import Cliente

class TestGerador(unittest.TestCase):

    NOME_ARQUIVO = "unittest.pkl"

    def test_gravacao_clientes(self):
        # Gera os clientes
        gerar_lote_clientes(self.NOME_ARQUIVO, 100)

        # Verifica, se todos os clientes foram salvos e
        # podem ser lidos
        clientes = ler_clientes(self.NOME_ARQUIVO, 100)
        for cliente in clientes:
            self.assertTrue(isinstance(cliente, Cliente))

        # Tenta ler um cliente a mais do que é possível
        with self.assertRaises(StopIteration):
            next(clientes)

        # Apaga o arquivo criado
        os.remove(self.NOME_ARQUIVO)

if __name__ == '__main__':
    unittest.main()
