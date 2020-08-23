from flask import (
	render_template,request, redirect,
	session, current_app, abort, jsonify,
)

from app.model.user import User
from app.model.vaga import PreVaga


def addVaga():
	if not 'user_id' in session:
		return abort(404)
	user = User.query.filter_by(id=session['user_id']).first()
	if user:
		if request.method == 'POST':
			data = {}
			if request.form:
				data['tel'] = request.form['tel']
				data['nome'] = request.form['nome']
				data['email'] = request.form['email']
				data['vagas'] = request.form['vagas']
				data['cidade'] = request.form['cidade']
				data['estado'] = request.form['estado']
				data['empresa'] = request.form['empresa']
				data['salario'] = request.form['salario']
				data['categoria'] = request.form['categoria']
				data['requisitos'] = request.form['requisitos']
				
			if request.json:
				data = request.json['vaga']
				
			if data:
				tel = data['tel']
				nome = data['nome']
				email = data['email']
				vagas = data['vagas']
				cidade = data['cidade']
				estado = data['estado']
				empresa= data['empresa']
				salario = data['salario']
				categoria = data['categoria']
				requisitos = data['requisitos']
				
				if nome and email and cidade and estado and categoria and requisitos:
				
					vaga=PreVaga(
						tel=tel,
						nome=nome,
						email=email,
						vagas=vagas,
						cidade=cidade,
						estado=estado,
						empresa=empresa,
						salario=salario,
						categoria=categoria,
						requisitos=requisitos
					)
					
					current_app.db.session.add(vaga)
					current_app.db.session.commit()
					return jsonify(vaga.id), 201
					
				else:
					return jsonify('dados incompletos'),206
			else:
				return jsonify('dados incompletos'),206
		
		return render_template("addvaga.html",user=user),200
		
	else:
		return abort(404)