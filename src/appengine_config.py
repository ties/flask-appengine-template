import gae_mini_profiler.profiler
gae_mini_profiler_ENABLED_PROFILER_EMAILS = ['user@example.org']

def webapp_add_wsgi_middleware(app):
    """Called with each WSGI handler initialisation"""
    app = gae_mini_profiler.profiler.ProfilerWSGIMiddleware(app)
    return app