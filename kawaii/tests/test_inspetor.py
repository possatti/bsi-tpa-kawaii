import unittest
import os

from kawaii import inspetor
from kawaii import persistencia
from kawaii import gerador
from kawaii.cliente import Cliente

class TestInspetor(unittest.TestCase):

    NOME_ARQUIVO_DESORDENADO = 'clientes-em-desordem.pkl'
    NOME_ARQUIVO_ORDENADO = 'clientes-em-ordem.pkl'
    QUANTIDADE_DE_CLIENTES = 0

    def setUp(self):
        # Gera uma lista de clientes desordenados e garante que ela
        # possui clientes em uma sequencia desordenada
        clientes_desordenados = list(gerador.produzir_clientes(self.QUANTIDADE_DE_CLIENTES))
        clientes_desordenados.append(Cliente(1, 'Lucas', 'Possatti', 'Guatemala', '12345678', 111))
        clientes_desordenados.append(Cliente(3, 'Mateus', 'Possatti', 'Guatemala', '12345678', 333))
        clientes_desordenados.append(Cliente(2, 'Davi', 'Possatti', 'Guatemala', '12345678', 222))
        self.QUANTIDADE_DE_CLIENTES += 3

        # Cria uma lista de clientes ordenados, baseando-se na
        # lista de clientes desordenados
        clientes_ordenados = sorted(clientes_desordenados)

        # Cria um arquivo de clientes desordenados
        with open(self.NOME_ARQUIVO_DESORDENADO, 'wb') as arq:
            persistencia.gravar_clientes(arq, clientes_desordenados)

        # Cria um arquivo de clientes ordenados
        with open(self.NOME_ARQUIVO_ORDENADO, 'wb') as arq:
            persistencia.gravar_clientes(arq, clientes_ordenados)

    def tearDown(self):
        # Apaga os arquivos de teste
        os.remove(self.NOME_ARQUIVO_ORDENADO)
        os.remove(self.NOME_ARQUIVO_DESORDENADO)

    def test_quantidade_de_clientes(self):
        """Verifica a quantidade de clientes dentro do arquivo"""

        with open(self.NOME_ARQUIVO_DESORDENADO, 'rb') as arq:
            # Conta quantos clientes há no arquivo
            quantidade = inspetor.quantidade_de_clientes(arq)

            # Verifica se a quantidade de clientes é a mesma
            # de quanto o arquivo foi criado
            self.assertTrue(quantidade == self.QUANTIDADE_DE_CLIENTES)

    def test_estao_ordenados(self):
        """
        Verifica se o arquivo desordenado, realmente está
        desordenado. E se o arquivo ordenado, realmente está
        ordenado.
        """

        # Verifica se o arquivo desordenado está desordenado
        with open(self.NOME_ARQUIVO_DESORDENADO, 'rb') as arq:
            self.assertFalse(inspetor.estao_ordenados(arq))

        # Verifica se o arquivo ordenado realmente está ordenado
        with open(self.NOME_ARQUIVO_ORDENADO, 'rb') as arq:
            self.assertTrue(inspetor.estao_ordenados(arq))

    def test_tamanho_do_arquivo(self):
        """
        Verifica se o tamanho de um dos arquivos é maior que
        zero.
        """
        self.assertTrue(inspetor.tamanho_do_arquivo(self.NOME_ARQUIVO_DESORDENADO) > 0)

if __name__ == '__main__':
    unittest.main()
