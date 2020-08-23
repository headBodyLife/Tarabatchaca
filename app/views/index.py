from flask import (
	render_template, session,
)

from app.model.user import User
from app.model.vaga import PreVaga

def index():
	user = None
	if "user_id" in session:
		user = User.query.filter_by(id=session['user_id']).first()
	if not user:
		session.pop('user_id',None)
	vagas=[]
	vagasTmp = PreVaga.query.all()
	for vaga in vagasTmp:
		vagas.append(vaga.get_vaga())
	return render_template('index.html',user=user,vagas=vagas)