
class Cliente:

	def __init__(self, nome, sobrenome, endereco, telefone, saldo):
		self.nome = nome
		self.sobrenome = sobrenome
		self.endereco = endereco
		self.telefone = telefone
		self.saldo = saldo

	def __str__(self):
		return "[" + \
			"nome: " + self.nome + ", " \
			"sobrenome: " + self.sobrenome + ", " \
			"endereco: " + self.endereco + ", " \
			"telefone: " + self.telefone + ", " \
			"saldo: " + str(self.saldo) + "]"
