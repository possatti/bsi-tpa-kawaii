"""Conjunto de métodos para inspeção dos arquivos de cliente."""

import os

from kawaii.cliente import Cliente
from kawaii import persistencia

def quantidade_de_clientes(arquivo):
	"""Informa a quantidade de clientes que há no arquivo"""

	quantidade = 0
	for cliente in persistencia.fornecer_clientes(arquivo):
		quantidade += 1
	return quantidade

def estao_ordenados(arquivo):
	"""
	Retorna verdadeiro se, e apenas se, os clientes estiverem
	ordenados dentro do arquivo.
	"""

	# Separa o iterador de clientes
	clientes = persistencia.fornecer_clientes(arquivo)

	# Itera através de todos os clientes, verificando se
	# eles estão na devida ordem
	anterior = next(clientes)
	for cliente in clientes:
		# Retorna falso se houver qualquer cliente fora de
		# ordem no arquivo
		if anterior > cliente:
			return False
		anterior = cliente

	# Retorna verdadeiro apenas, se todos estiverem ordenados
	return True

def tamanho_do_arquivo(caminho_para_o_arquivo):
	"""Informa qual o tamanho do arquivo específicado"""

	return os.path.getsize(caminho_para_o_arquivo)
