from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)


from url import routes, models