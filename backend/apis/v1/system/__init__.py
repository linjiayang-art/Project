from flask.views import MethodView
from flask import jsonify
from backend.apis.v1 import api_v1

class IndexAPI(MethodView):


    def get(self):
        return jsonify({
            "api_version": "1.0",
            "api_base_url": "http://example.com/api/v1",
        
        })
    
api_v1.add_url_rule('/',view_func=IndexAPI.as_view('index'),methods=['GET'])