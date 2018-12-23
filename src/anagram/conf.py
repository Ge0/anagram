import os
import importlib

_settings_module = os.environ.get("ANAGRAM_SETTINGS_MODULE")

if _settings_module is None:
    settings = importlib.import_module(".config.dev", package="anagram")
else:
    settings = importlib.import_module(_settings_module)
