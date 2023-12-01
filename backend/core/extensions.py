from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_mailman import Mail
#from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager


db=SQLAlchemy()
csrf=CSRFProtect()
mail=Mail()
#toolbar=DebugToolbarExtension()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from  backend.models.system import UserInfo
    user = db.session.get(UserInfo, int(user_id))
    return user

login_manager.login_view = 'auth.login'
login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'