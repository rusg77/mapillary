from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import get_config

app = Flask(__name__)
app.config.from_object(get_config())
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models.user import User
from app.routes.user import *
from app.routes.web import *

if app.config['ENV'] == 'dev':
    from app.routes.automation import *
