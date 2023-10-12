from flask import Flask

import os
from backend.core.extensions import db,csrf,mail
#.core 
#from backend.core.commands import register_commands
from backend.core.errors import register_errors
from backend.core.logging import register_logging
from backend.core.request import register_request_handlers
from backend.settings import basedir

#settings
from backend.settings import config

#BLUEPRINT
from backend.apis.v1 import  api_v1

def create_app(config_name):

    app=Flask('backend')
    app.config.from_object(config[config_name])
    app.before_request
    #extensions
    db.init_app(app=app)
    csrf.init_app(app)
    mail.init_app(app)
    #login_manager.init_app(app)
    

    #blueprints
    app.register_blueprint(api_v1,url_prefix='/api/v1')


    #register
    if app.debug==False:
        register_errors(app=app)
    register_logging(app=app)
    register_request_handlers(app=app)  

    return app

    