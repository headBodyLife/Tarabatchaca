
from flask import (
	render_template, session,
)

from app.model.user import User

def dashboard():
	user = None
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		if not user:
			session.pop('user_id',None)
			return redirect('/login/')
	
	return render_template('dashboard.html',user='etho')