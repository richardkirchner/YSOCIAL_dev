from flask import Flask, Blueprint
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager
# from app.events.models import event
# from app.users.models import users
from . import events, api, users

from app.events.routes import blueprint as events_blueprint
from app.api.routes import blueprint as api_blueprint

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')
  register_extensions(app)
  register_blueprints(app)

  return app

def register_blueprints(app: Flask):
  app.register_blueprint(events_blueprint)
  app.register_blueprint(users.routes.blueprint)
  app.register_blueprint(api_blueprint)

def register_extensions(app:Flask):
  login_manager.init_app(app)
  db.init_app(app)
  with app.app_context():
      from app.events.models import event
      db.create_all()
      migrate.init_app(app, db, compare_type=True)
