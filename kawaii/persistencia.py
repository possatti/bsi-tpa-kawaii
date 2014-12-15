"""Conjunto de métodos para persistência dos clientes."""

import pickle

def ler_clientes(arquivo):
	"""
	Lê do arquivo todos os clientes, de uma única vez para
	a mémória. O retorno será uma lista preenchida com todos
	os clientes	do arquivo, na ordem em que foram lidos.
	"""

	# Inicia um unpickler
	unpickler = pickle.Unpickler(arquivo)

	# Lê os clientes contidos no arquivo, até chegar o final
	# do arquivo
	clientes = []
	while True:
		# Tenta ler mais um cliente
		try:
			cliente = unpickler.load()
			clientes.append(cliente)
		# Caso o final do arquivo tenha chegado, encerramos a
		# leitura
		except EOFError:
			break

	# Retorna todos os clientes lidos
	return clientes

def fornecer_clientes(arquivo):
	"""
	Método gerador que lê o arquivo enquanto fornece, um por
	um, os clientes daquele arquivo. Para um aproveitamento
	melhor, sugere-se usar um arquivo com buffer de leitura.
	"""

	# Inicia um unpickler
	unpickler = pickle.Unpickler(arquivo)

	# Lê os clientes contidos no arquivo, até chegar o final
	# do arquivo
	while True:
		# Tenta ler mais um cliente
		try:
			cliente = unpickler.load()
			yield cliente
		# Caso o final do arquivo tenha chegado, encerramos a
		# leitura
		except EOFError:
			break

def gravar_clientes(arquivo, clientes):
	"""
	Grava os clientes em um arquivo. A lista de clientes
	será iterada, então é possível receber um gerador que
	forneça os clientes.
	"""

	# Criar um pickler usando o protocolo mais alto disponível
	pickler = pickle.Pickler(arquivo, pickle.HIGHEST_PROTOCOL)

	# Grava os clientes no arquivo
	for cliente in clientes:
		pickler.dump(cliente)

if __name__ == "__main__":
	### TESTE ###

	print(':: INICIANDO O TESTE ::\n')
	from kawaii import gerador

	# Gera alguns clientes para o teste
	#gerador.gerar_lote_clientes('clientes-teste.pkl', 7, buffer_size=-1)
	with open('clientes-teste.pkl', 'wb') as arq:
		gravar_clientes(arq, gerador.produzir_clientes(3))

	# Abre o arquivo com os clientes
	with open('clientes-teste.pkl', 'rb') as arq:
		# Lê os clientes, e conta quantos são
		quantidade = 0
		for cliente in fornecer_clientes(arq):
			quantidade += 1
			print('CLIENTE: ', cliente)
		print(quantidade, 'clientes lidos.')
