#!/usr/bin/python3

import random
import pickle
from cliente import Cliente

def get_random_letter():
	return random.choice("abcdefghijklmnopqrstuvwxyz")

def get_random_string(length):
	string = ""
	for _ in range(length):
		string += get_random_letter()
	return string

def get_random_integer():
	return random.choice("0123456789")

def get_random_integers(number):
	string = ""
	for _ in range(number):
		string += get_random_integer()
	return string

def gerar_cliente():
	nome = get_random_string(10)
	sobrenome = get_random_string(20)
	endereco = get_random_string(30)
	telefone = get_random_integers(8)
	saldo = random.randrange(-1000, 1000001)
	return Cliente(nome, sobrenome, endereco, telefone, saldo)

def gerar_lote_clientes(numero, caminho_arquivo, tamanho_buffer=-1):
	# Abre o arquivo
	with open(caminho_arquivo, 'wb', buffering=tamanho_buffer) as arquivo:
		# Criar um pickler usando o protocolo mais alto
		pickler = pickle.Pickler(arquivo, pickle.HIGHEST_PROTOCOL)

		# Cria e grava cada cliente no arquivo
		gravados = 0
		while gravados < numero:
			cliente = gerar_cliente()
			pickler.dump(cliente)
			gravados += 1

def ler_clientes(numero_clientes, caminho_arquivo):
	'''
	Lê o número específicado de clientes para uma lista. O
	problema disso é a lista iria ocupar muita memória. Mas
	se isso não for um problema, esse método pode ser útil.
	'''

	# Abre o arquivo
	with open(caminho_arquivo, 'rb') as arquivo:
		# Inicia um unpickler
		unpickler = pickle.Unpickler(arquivo)

		# Lê o número específicado de clientes para uma lista
		lidos = 0
		clientes = []
		while lidos < numero_clientes:
			cliente = unpickler.load()
			clientes.append(cliente)
			lidos += 1

		# Retorna todos os clientes lidos
		return clientes
