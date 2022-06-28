from flask import Flask
from .site.routes import site
from .api.routes import api
from config import Config

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(api)

app.config.from_object(Config)