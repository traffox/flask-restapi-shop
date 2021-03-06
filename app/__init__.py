from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True
key = os.getenv("JWT_SECRET_KEY")
app.config["SECRET_KEY"] = f"{key}"

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

from app.catalog.views import catalog

app.register_blueprint(catalog)

# migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
