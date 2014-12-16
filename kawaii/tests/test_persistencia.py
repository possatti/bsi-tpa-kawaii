import unittest
import os

from kawaii import persistencia
from kawaii import gerador
from kawaii.cliente import Cliente

class TestPersistencia(unittest.TestCase):

    QUANTIDADE_DE_CLIENTES = 3
    NOME_ARQUIVO = 'clientes-teste.pkl'

    def setUp(self):
        # Cria alguns clientes
        self.clientes = list(gerador.produzir_clientes(self.QUANTIDADE_DE_CLIENTES))

        # Grava os clientes
        with open(self.NOME_ARQUIVO, 'wb') as arq:
            persistencia.gravar_clientes(arq, self.clientes)

    def tearDown(self):
        os.remove(self.NOME_ARQUIVO)

    def test_ler_clientes(self):
        # Lê os clientes contidos no arquivo
        with open(self.NOME_ARQUIVO, 'rb') as arq:
            clientes_lidos = persistencia.ler_clientes(arq)

        # Compara com a lista de clientes originais
        self.assertTrue(clientes_lidos == self.clientes)

    def test_fornecer_clientes(self):
        # Lê os clientes contidos no arquivo
        with open(self.NOME_ARQUIVO, 'rb') as arq:
            clientes_lidos = list(persistencia.fornecer_clientes(arq))

        # Compara com a lista de clientes originais
        self.assertTrue(clientes_lidos == self.clientes)

    def test_gravar_clientes(self):
        # Cria alguns clientes
        clientes = gerador.produzir_clientes(self.QUANTIDADE_DE_CLIENTES)

        # Grava os clientes
        with open('clientes-teste-gravacao.pkl', 'wb') as arq:
            persistencia.gravar_clientes(arq, clientes)

        # Verifica se foram gravados corretamente
        with open('clientes-teste-gravacao.pkl', 'rb') as arq:
            clientes_lidos = persistencia.fornecer_clientes(arq)

            # Conta quantos clientes há no arquivo, e verifica
            # se cada objeto é realmente uma instância de Cliente
            lidos = 0
            for cliente in clientes_lidos:
                lidos += 1
                self.assertTrue(isinstance(cliente, Cliente))
            self.assertTrue(lidos == self.QUANTIDADE_DE_CLIENTES)

        # Apaga o arquivo de teste
        os.remove('clientes-teste-gravacao.pkl')

if __name__ == '__main__':
    unittest.main()
