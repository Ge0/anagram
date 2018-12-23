"""Generate anagrams from names."""
from flask import jsonify, render_template, request

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

from .anagram import find_anagrams
from .conf import settings
from .errors import AnagramError

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


@app.route('/about')
def about():
    return render_template("about/template.html")


@app.route("/generate", methods=["POST"])
def generate():
    fullname = request.form.get("fullname", "")
    if not fullname:
        return jsonify({"error": "name is empty"})
    else:
        try:
            names = [f"{first_name} {last_name}"
                     for (first_name, last_name)
                     in find_anagrams(fullname, settings.FIRST_NAMES,
                                      settings.LAST_NAMES)]
        except AnagramError as exn:
            return jsonify({"error": str(exn)})
        else:
            return jsonify({"results": names})
