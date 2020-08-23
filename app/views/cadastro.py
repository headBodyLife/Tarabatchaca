from flask import (
	render_template,request, session,
	current_app, redirect,
)

from app.model.user import User


def cadastro():
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		if not user:
			session.pop('user_id',None)
		else:
			return redirect('/')
			
	if request.method == 'POST':
		data = {}
		if request.json:
			data = request.json['user']
		elif request.form:
			data['tel'] = request.form['tel']
			data['nome'] = request.form['Nome']
			data['senha'] = request.form['senha']
			data['senha'] = request.form['senha']
			data['email'] = request.form['email']
			data['usuario'] = request.form['username']
			
		if data:
			tel = data['tel'] if data['tel'] else None
			nome = data['nome'] if data['nome'] else None
			email = data['email'] if data['email'] else None
			senha1 = data['senha'] if data['senha'] else None
			senha2 = data['senha'] if data['senha'] else None
			usuario = data['username'] if data['username'] else None
			
			
			if nome:
				ver_senha = senha(senha1,senha2)
				if ver_senha[0]:
					ver_user = Usuario(usuario)
					if ver_user[0]:
						ver_email = Email(email)
						if ver_email[0]:
							new_user = User(
								tel=tel, nome=nome,
								senha=senha1, email=email,
								usuario=usuario,img=None
								)
							current_app.db.session.add(new_user)
							current_app.db.session.commit()
							session['user_id'] = new_user.id
							return 'ok',201
					
						else:
							return {'erro':ver_email[1]},206
					else:
						return {'erro':ver_user[1]},206
				else:
					return  {'erro':ver_senha[1]},206
			else:
				return {'erro':'nome Inválido'},206
		else:
			return {'erro':'sem conteudo'},204
	
	return render_template('cad.html'),200


# Válida a senha
def senha(senha1, senha2):
	if senha1:
		if senha1 == senha2:
			if len(senha1) > 7:
				if not senha1.isalnum():
					conf = False
					for i in list(senha1):
						if i.isupper():
							conf = True
							break
					if conf:
						return [True,senha1]
					else:
						return [False,'A senha deve contar ao menos uma letra maiuscula']
				else:
					return [False,'A senha deve contar ao menos um carácter especial']
			else:
				return [False,'a senha deve conter mais de 8 caracteres']
		else:
			return [False,'as senhas não coincidem!']
	else:
		return [False,'O campo SENHA não pode ficar vazio']



# Validação Usuário 
def Usuario(user):
	if user:
		if not User.query.filter_by(usuario=user).first():
			if len(user) > 8:
				if not ' ' in user:
					return [True, user]
				else:
					return [False,'campo usuario não pode conter espaços']
			else:
				return [False,'O campo usuario deve conter mais de 8 caracteres ']
		else:
			return [False,' Usuario Indisponível']
	else:
		return [False,'O campo usuario não pode ficar vazio']
	


# Validação Email
def Email(email):
	if email:
		if not User.query.filter_by(email=email).first():
			if len(email) > 8:
				if not ' ' in email:
					if '@' in email:
						var = email.split('@')[1]
						if len(var) > 6:
							return [True, email]
						return [False,' Email Inválido']
					else:
						return [False, 'Email Inválido']
				else:
					return [False,'campo email não pode conter espaços']
			else:
				return [False,'O campo email deve conter mais de 8 caracteres ']
		else:
			return [False,' Email Indisponível']
	else:
		return [False,'O campo email não pode ficar vazio']