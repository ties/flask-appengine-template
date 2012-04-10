"""
Initialize Flask app

"""

from flask import Flask
from gae_mini_profiler import profiler

app = Flask('application')
app.config.from_object('application.settings')

def get_request_id():
    return profiler.request_id
app.jinja_env.globals['get_request_id'] = get_request_id

import urls
