"""Generate anagrams from names."""
from flask import render_template

from .__about__ import (
    __author__,
    __copyright__,
    __email__,
    __license__,
    __summary__,
    __title__,
    __uri__,
    __version__,
)

from ._app import app

__all__ = [
    "__author__",
    "__copyright__",
    "__email__",
    "__license__",
    "__summary__",
    "__title__",
    "__uri__",
    "__version__",
    "app",
]

@app.route('/')
def index():
    return render_template("index/template.html")


@app.route("/generate")
def generate():
    pass
