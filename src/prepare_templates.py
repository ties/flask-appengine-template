"""
Precompile the Jinja2 templates

Based on example code from https://github.com/mitsuhiko/flask/issues/101
"""
import os, sys
from jinja2 import Environment, PackageLoader

SDK_PATH = '/home/ties/Dev/Tools/google_appengine/'

# Prevent errors caused by gae_mini_profiler which asserts that SERVER_SOFTWARE is in os.environ.
# also trick application/settings.py into setting up the debug version of the app.
os.environ['SERVER_SOFTWARE'] = "Dev ..."

def logger(m, *args, **kw):
    print m

def compile_template(dest):
    from application import app
    app.debug = True
    app.jinja_env.compile_templates(dest, log_function=logger, zip='stored')


if __name__ == '__main__':
    sys.path.insert(0, SDK_PATH)
    import dev_appserver
    dev_appserver.fix_sys_path()
    compile_template("compiled_templates.zip")