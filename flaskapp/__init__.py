from flask import Flask
from flaskapp.config import Config
from flaskapp.api.tables import db

def create_app():
  app = Flask(__name__)

  app.config.from_object(Config)

  db.init_app(app)

  from flaskapp.main.routes import main
  from flaskapp.api.routes import backend

  app.register_blueprint(main)
  app.register_blueprint(backend)

  return app