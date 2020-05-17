from flask import Flask 

def create_app(config_filename):
  app = Flask(__name__)
  app.config.from_envvar('FLASK_APP_CONFIG')

  from project.model import db
  db.init_app(app)

  @app.route('/')
  def index():
    return 'Test'

  return app