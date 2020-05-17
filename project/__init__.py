from flask import Flask 

def create_app(config_filename):
  app = Flask(__name__)

  @app.route('/')
  def index():
    return 'Test'

  return app