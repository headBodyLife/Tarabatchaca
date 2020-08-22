

from flask import render_template


def config_errPage(app):
	@app.errorhandler(404)
	def err404(arg=None):
		return render_template('errorPage.html')