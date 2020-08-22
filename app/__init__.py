import flask
from .model import config_db
from .views import config_vw


def create_app():
	app = flask.Flask(__name__.split('.')[0])
	
	app.config["SECRET_KEY"] = 'UAJAjaianbbUuyhJJI'
	
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.template_folder = "front/templates/"
	app.static_folder = "front/static/"

	

	config_vw(app)
	config_db(app)
	
	return app
