from flask_sqlalchemy.record_queries import get_recorded_queries
from flask import request



def register_request_handlers(app):
    @app.after_request
    def query_profiler(response):
        for q in get_recorded_queries():
            if q.duration >=app.config['BACKEND_SLOW_QUERY_THRESHOLD']:
                app.logger.warning(
                    'Slow query: Duration'
                    f'{q.duration:f}s\n Context:{q.location}\nQuery:{q.statement}\n'
                )
        return response
#before request record 
"""     @app.before_request
    def before_record():
        return None
 """