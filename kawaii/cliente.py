from functools import total_ordering

@total_ordering
class Cliente:

	def __init__(self, numero, nome, sobrenome, endereco, telefone, saldo):
		self.numero = numero
		self.nome = nome
		self.sobrenome = sobrenome
		self.endereco = endereco
		self.telefone = telefone
		self.saldo = saldo

	def __str__(self):
		return "[" + \
			"numero: " + str(self.numero) + ", " \
			"nome: " + self.nome + ", " \
			"sobrenome: " + self.sobrenome + ", " \
			"endereco: " + self.endereco + ", " \
			"telefone: " + self.telefone + ", " \
			"saldo: " + str(self.saldo) + "]"

	def __eq__(self, other):
		return (
			(self.numero,
			self.nome.lower(),
			self.sobrenome.lower(),
			self.endereco.lower(),
			self.telefone.lower(),
			self.saldo) ==
				(other.numero,
				other.nome.lower(),
				other.sobrenome.lower(),
				other.endereco.lower(),
				other.telefone.lower(),
				other.saldo))

	def __lt__(self, other):
		return (
			(self.saldo,
			self.numero,
			self.nome.lower(),
			self.sobrenome.lower(),
			self.endereco.lower(),
			self.telefone.lower()) <
				(other.saldo,
				other.numero,
				other.nome.lower(),
				other.sobrenome.lower(),
				other.endereco.lower(),
				other.telefone.lower()))
