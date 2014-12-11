import unittest
import random
from algoritmos import *
from gerador import gerar_cliente
from cliente import Cliente

class TestAlgoritmos(unittest.TestCase):

    def setUp(self):
        # Define uma seed estática para ajudar no determinismo ;)
        random.seed(5)

        # Cria uma lista desordenada
        self.caos = []
        for i in range(100):
            self.caos.append(random.randint(0,100))

        # Copia a lista, e ordena a nova lista
        self.ordem = self.caos[:]
        self.ordem.sort()

        # Verifica que as duas listas são diferentes
        assert(self.caos is not self.ordem)

    def test_pythonsort(self):
        '''Testa o método de ordenação normal do python.'''
        
        lista = self.caos[:]
        lista.sort()
        self.assertTrue(lista == self.ordem)

    def test_selectsort(self):
        lista = self.caos[:]
        selectsort(lista)
        self.assertTrue(lista == self.ordem)

    def test_insertionsort(self):
        lista = self.caos[:]
        insertionSort(lista)
        self.assertTrue(lista == self.ordem)

    def test_quicksort_simple(self):
        lista = self.caos[:]
        lista = quicksort_simple(lista)
        self.assertTrue(lista == self.ordem)

    def test_quicksort_inplace(self):
        lista = self.caos[:]
        quicksort_inplace(lista, 0, len(lista) - 1)
        self.assertTrue(lista == self.ordem)

    def test_qsort(self):
        lista = self.caos[:]
        lista = qsort(lista)
        self.assertTrue(lista == self.ordem)
        pass

    def test_shellsort(self):
        lista = self.caos[:]
        shellSort(lista)
        self.assertTrue(lista == self.ordem)

    def test_sort_shell(self):
        lista = self.caos[:]
        sort_shell(lista)
        self.assertTrue(lista == self.ordem)

    def test_insertionsort_clientes(self):
        '''
        Faz o teste do insertionSort, usando os clientes. Apenas
        para verificar que é possível aplicar o algoritmo em
        instâncias da classe.
        '''

        # Cria uma lista desordenada de clientes
        clientes_caos = []
        for i in range(100):
            clientes_caos.append(gerar_cliente())

        # Copia a lista, e ordena a nova lista
        clientes_ordem = clientes_caos[:]
        clientes_ordem.sort()
        
        # Verifica que as duas listas são diferentes
        assert(clientes_caos is not clientes_ordem)

        # Copia a lista de clientes desordenada e a ordena
        clientes_lista = clientes_caos[:]
        insertionSort(clientes_lista)
        self.assertTrue(clientes_lista == clientes_ordem)

if __name__ == '__main__':
    unittest.main()
