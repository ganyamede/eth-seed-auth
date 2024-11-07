import logging
from flask import Flask
from flask_cors import CORS
from datetime import timedelta
from core.env.config import SECRET_KEY
from core.Application.routes import App
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', 
    filename='core/storage/path/core.log',
    filemode='a'
)

app = Flask(__name__, template_folder='core/Application/templates')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=3650) 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
app.config["JWT_SECRET_KEY"] = SECRET_KEY
app.secret_key = SECRET_KEY
app.register_blueprint(App) 
jwt = JWTManager(app)
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)