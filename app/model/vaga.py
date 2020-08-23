from . import db

from cryptography.fernet import Fernet 
KEY = b'-_EMYuoHzkG-80-nHfz412mIJfWIQkMuGDqnlLaW3KY='


from datetime import datetime

class Vaga(db.Model):
	
	__tablename__='vagas'
	
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.Unicode,nullable=False) # da vaga
	email = db.Column(db.Unicode,nullable=False)# email da empresa
	vagas = db.Column(db.Integer,nullable=False) # quant
	empresa = db.Column(db.Unicode,nullable=False)# nome da empresa
	salario = db.Column(db.Unicode,nullable=False) # salário
	requisitos = db.Column(db.Text,nullable=False) #text
	disponivel = db.Column(db.String(64),nullable=False) # boolean
	
	def __init__(
		self, nome, email, vagas, disponivel,
		empresa, salario, requisitos, categoria):
	
		self.nome = nome
		self.vagas = vagas
		self.categoria = categoria
		self.disponivel = disponivel
		
		self.email = self.encrypt(email)
		self.empresa = self.encrypt(empresa)
		self.salario = self.encrypt(salario)
		self.requisitos = self.encrypt(requisitos)
	
	
	def encrypt(self,msg):
		return Fernet(KEY
			).encrypt(bytes(msg,'utf-8'))
	
	def decrypt(self,msg):
		return Fernet(KEY
			).decrypt(msg).decode('utf-8')
	
	
	def get_vaga(self):
		return {
			"id": self.id,
			"nome": self.nome,
			"vagas": self.vagas,
			'disponivel': self.disponivel,
			
			"email": self.decrypt(self.email),
			"salario": self.decrypt(self.salario),
			"empresa": self.decrypt(self.empresa),
			"requisitos": self.decrypt(self.requisitos),
		}
		
	

class PreVaga(db.Model):
	
	__tablename__='preVagas'
	
	id = db.Column(db.Integer, primary_key=True)
	vagas = db.Column(db.Integer,nullable=False) # quant
	
	tel = db.Column(db.Unicode,nullable=False)# tel da empresa
	nome = db.Column(db.Unicode,nullable=False) # da vaga
	email = db.Column(db.Unicode,nullable=False)# email da empresa
	cidade = db.Column(db.Unicode,nullable=False)# nome da empresa
	estado = db.Column(db.Unicode,nullable=False)# nome da empresa
	empresa = db.Column(db.Unicode,nullable=False)# nome da empresa
	salario = db.Column(db.Unicode,nullable=False) # salário
	categoria = db.Column(db.String(128),nullable=False)
	data = db.Column(db.Date, nullable=False)
	requisitos = db.Column(db.Text,nullable=False) #text
	disponivel = db.Column(db.String(64),nullable=False) # boolean
	
	def _get_data(self):
		return datetime.now()
	
	def __init__(
		self, nome, email, vagas,
		empresa, salario, requisitos,
		categoria,
		tel, cidade, estado, ):
	
		self.nome = nome
		self.vagas = vagas
		self.categoria = categoria
		self.disponivel = 1
		self.data = self._get_data()
		
		self.tel = self.encrypt(tel)
		self.email = self.encrypt(email)
		self.cidade = self.encrypt(cidade)
		self.estado = self.encrypt(estado)
		self.empresa = self.encrypt(empresa)
		self.salario = self.encrypt(salario)
		self.requisitos = self.encrypt(requisitos)
	
	
	def encrypt(self,msg):
		return Fernet(KEY
			).encrypt(bytes(msg,'utf-8'))
	
	def decrypt(self,msg):
		return Fernet(KEY
			).decrypt(msg).decode('utf-8')
	
	
	def get_vaga(self):
		return {
			"id": self.id,
			"nome": self.nome,
			'data': self.data,
			"vagas": self.vagas,
			'categoria': self.categoria,
			'disponivel': self.disponivel,
			
			'tel': self.decrypt(self.tel),
			'cidade': self.decrypt(self.cidade),
			'estado': self.decrypt(self.estado),
			"email": self.decrypt(self.email),
			"salario": "R$"+str(self.decrypt(self.salario))+",00" if self.decrypt(self.salario) else 'A combinar',
			"empresa": self.decrypt(self.empresa),
			"requisitos": self.decrypt(self.requisitos),
		}