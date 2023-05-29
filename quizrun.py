from werkzeug.serving import run_simple
from app import *

run_simple('localhost', 5004, app, use_reloader=True, threaded=True)