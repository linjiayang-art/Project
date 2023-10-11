from flask import jsonify,make_response
from flask_wtf.csrf import CSRFError

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify(code='400',msg=error.description,data=None),400)
    
    @app.errorhandler(404)
    def page_not_found(error):
        return  jsonify(code='404',msg=error.description,data=None),404

    @app.errorhandler(500)
    def internal_server_error(error):
        return make_response(jsonify(code='500',msg=error.description,data=None),500)

    @app.errorhandler(CSRFError)
    def handle_csrf_error(error):
        return make_response(jsonify(code='400',msg=error.description,data=None),400)