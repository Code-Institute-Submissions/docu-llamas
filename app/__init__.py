from app import routes
from app import routes, models, errors
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
