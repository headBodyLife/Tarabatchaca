from flask import (
	render_template, abort,
	session, redirect,
)

from app.model.user import User
from app.model.vaga import PreVaga

def descricao(vaga = False):
	user = None
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		if not user:
			session.pop('user_id',None)
	if vaga:
		if isinstance(vaga,int):
			vaga = PreVaga.query.filter_by(id=vaga).first()
			if vaga:
				return render_template(
					'desc.html',vaga=vaga.get_vaga(),
					user=user,
				)
			else:
				return abort(404)
		else:
			return abort(404)
	else:
		return abort(404)