from flask import Flask

from .conf import settings

app = Flask(__name__,
            static_url_path="/public",
            static_folder=settings.PUBLIC_DIR)
app.secret_key = settings.FLASK_SECRET_KEY.encode()
app.testing = settings.TESTING
