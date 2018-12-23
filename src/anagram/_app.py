from flask import Flask

from .conf import settings

app = Flask(__name__)
app.secret_key = settings.FLASK_SECRET_KEY.encode()
app.testing = settings.TESTING
