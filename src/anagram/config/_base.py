"""Base configuration."""
from collections import defaultdict
import os
from pathlib import Path

from ..anagram import load_file

RESOURCES_DIR = Path(__file__).parents[0] / ".." / "resources"
PUBLIC_DIR = Path(__file__).parents[0] / ".." / ".." / ".." / "public"

FLASK_SECRET_KEY = os.environ["FLASK_SECRET_KEY"]  # Must be set in env!

TESTING = True  # Change to False for production mode.

FIRST_NAMES = defaultdict(list)
LAST_NAMES = defaultdict(list)

load_file(RESOURCES_DIR / "FIRST_NAMES.txt", FIRST_NAMES)
load_file(RESOURCES_DIR / "FAMILY_NAMES_FR.txt", LAST_NAMES)
