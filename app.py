import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from backend import create_app  # noqa
from backend.settings import basedir



#check_file
LOG_DIR=os.path.join(os.path.abspath(basedir),'logs')
if not os.path.exists( LOG_DIR):
    os.makedirs( LOG_DIR)
UPLOAD_DIR=os.path.join(os.path.abspath(os.path.dirname(__file__)),'uploads')
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)

@app.route('/')
def index():
    return 'hello world'

app.run()