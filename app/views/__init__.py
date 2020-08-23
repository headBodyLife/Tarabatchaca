from .cadastro import cadastro
from .dashboard import dashboard
from .descricao import descricao
from .index import index
from .login import login, logout
from .vaga import addVaga
from .errors import config_errPage



from flask import (
	Blueprint
)

bp = Blueprint('webui',__name__.split('.')[0])

bp.add_url_rule(
	'/',
	methods=["GET"],
	view_func=index,
	endpoint="index",
)

bp.add_url_rule(
	'/cadastro/',
	methods=["GET","POST"],
	view_func=cadastro,
	endpoint="cadastro",
)

bp.add_url_rule(
	'/login/',
	methods=["GET","POST"],
	view_func=login,
	endpoint="login",
)

bp.add_url_rule(
	'/logout/',
	methods=["GET","POST"],
	view_func=logout,
	endpoint="logout",
)


bp.add_url_rule(
	'/dashboard/',
	methods=["GET","POST"],
	view_func=dashboard,
	endpoint="dashboard",
)

bp.add_url_rule(
	'/descricao/<int:vaga>/',
	methods=["GET","POST"],
	view_func=descricao,
	endpoint="descricao",
)

bp.add_url_rule(
	'/addVaga/',
	methods=["GET","POST"],
	view_func=addVaga,
	endpoint="addVaga",
)



def config_vw(app):
	app.register_blueprint(bp)
	config_errPage(app)