from flask import (
	render_template
)

def addVaga():
	return render_template("addvaga.html",user='etho')