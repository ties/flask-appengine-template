"""
Initialize Flask app

"""
import logging, os

from flask import Flask
from jinja2 import ModuleLoader
from gae_mini_profiler import profiler

# Use compiled templates as seen in <https://github.com/mitsuhiko/flask/issues/101>
class GAEFlask(Flask):
	def create_global_jinja_loader(self):
		if self.debug:
			return super(GAEFlask, self).create_global_jinja_loader()
		else:
			filename = 'compiled_templates.zip'
			logging.info("Loading templates from {}".format(filename))
			if not os.path.isfile(filename):
				raise TemplateNotFound("Missing {}".format(filename))
			return ModuleLoader(filename)

app = GAEFlask('application')
app.config.from_object('application.settings')

def get_request_id():
    return profiler.request_id
app.jinja_env.globals['get_request_id'] = get_request_id

import urls
