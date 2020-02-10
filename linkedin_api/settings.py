import os
import tempfile

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(tempfile.gettempdir(), "linkedin")
COOKIE_PATH = os.path.join(ROOT_DIR, "cookies/")
