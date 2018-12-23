"""Base configuration."""
import os

FLASK_SECRET_KEY = os.environ["FLASK_SECRET_KEY"]  # Must be set in env!

TESTING = True  # Change to False for production mode.
