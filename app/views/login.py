from flask import (
	render_template,session,
	redirect, request, jsonify
)

from app.model.user import User

def login():
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		if not user:
			session.pop('user_id',None)
		else:
			return redirect('/')
		
	if request.method == 'POST':
		data = {}
		if request.form:
			data['user']  = request.form["user"]
			data['senha'] = request.form["senha"]
		elif request.json:
			data = request.json["user"]
		if data['user'] and data['senha']:
			user = User.query.filter_by(email=data['user']).first()
			if not user:
				user = User.query.filter_by(usuario=data['user']).first()
			if user:
				if user.check_senha(data['senha']):
					session['user_id'] = user.id
					return 'ok', 200
				else:
					return jsonify({'erro':' Credenciais invalidas2'}), 200
			else:
				return jsonify({'erro':' Credenciais invalidas1'}), 200
		else:
			return jsonify({'erro':'Conteudo parcial'}), 200
				
	
	return render_template('login.html')

def logout():
	session.pop('user_id',None)
	return redirect('/')