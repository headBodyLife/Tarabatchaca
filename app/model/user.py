from . import db

from werkzeug.security import (
	generate_password_hash as gph,
	check_password_hash as cph,
)

from cryptography.fernet import Fernet
KEY = b'0csxY-kWDjV6SKBZAkP7v2GI7k3-xT0dn2MEuBwTYGo='


class User(db.Model):
	
	__tablename__="usuario"
	
	id = db.Column(db.Integer, primary_key=True)
	tel = db.Column(db.String(24))
	img = db.Column(db.BLOB)
	nome = db.Column(db.Unicode, nullable=False)
	email = db.Column(db.String(128),unique=True,nullable=False)
	senha = db.Column(db.Text,nullable=False)
	usuario = db.Column(db.String(128),unique=True,nullable=False)
	
	
		
	def get_user(self):
		return {
			'id': self.id,
			'tel': self.tel,
			'nome': self.decrypt(self.nome),
			'email': self.email,
			'usuario': self.usuario,
			'img': b64encode(
				self.img).decode(
				'ascii') if self.img else None,
		}
	
	
	
	def ger_senha(self,msg):
		return gph(msg)
	
	def check_senha(self,senha):
		return cph(self.senha,senha)
	
	
	
	def encrypt(self, msg):
		enc = Fernet(KEY)
		return enc.encrypt(bytes(msg,'utf-8'))
		
	def decrypt(self, msg):
		dec = Fernet(KEY)
		return dec.decrypt(msg).decode('utf-8')



	def __init__(
		self, tel, nome, email,
		senha, usuario, img, ):
			
		self.tel = tel
		self.img = img
		self.email = email
		self.usuario = usuario
		self.nome = self.encrypt(nome)
		self.senha = self.ger_senha(senha)
		
		
		
		