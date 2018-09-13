from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.main.controllers import main as main_module
app.register_blueprint(main_module)

db.create_all()