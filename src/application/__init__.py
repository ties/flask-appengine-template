"""
Initialize Flask app

"""

from flask import Flask
# Remove GAEMiniProfiler until flaskext.gae_mini_profiler incorporates upstream changes from <https://github.com/kamens/gae_mini_profiler/pull/16>
# from flaskext.gae_mini_profiler import GAEMiniProfiler

app = Flask('application')
app.config.from_object('application.settings')
#GAEMiniProfiler(app)

import urls
