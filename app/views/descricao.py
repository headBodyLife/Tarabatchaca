from flask import (
	render_template, abort
)

def descricao(vaga = False):
	if vaga:
		if isinstance(vaga,int):
			return render_template('desc.html',vaga=vaga,user='etho')
		else:
			return abort(404)
	else:
		return abort(404)