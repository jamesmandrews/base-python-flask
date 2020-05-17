from flask import Flask 
from flask_migrate import Migrate

def create_app(config_filename):
  app = Flask(__name__)
  app.config.from_envvar('FLASK_APP_CONFIG')

  from project.database import db
  db.init_app(app)
  migrate = Migrate(app, db)

  @app.route('/')
  def index():
    return 'Test'

  return app