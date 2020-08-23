from app.model.vaga import PreVaga
from app.model.user import User

from flask import (
	render_template, session,
)

from datetime import date, timedelta

def index():
	user = None
	if "user_id" in session:
		user = User.query.filter_by(id=session['user_id']).first()
	if not user:
		session.pop('user_id',None)
	vagas = []
	for c in range(4):
		vagas1=[]
		vagasTmp = PreVaga.query.filter_by(data=(date.today() - timedelta(c))).all()
		for vaga in vagasTmp:
			vagas1.append(vaga.get_vaga())
		if vagas1:
			vagas.append(vagas1)
	print(vagas)
	return render_template('index.html',user=user,vagas=vagas)