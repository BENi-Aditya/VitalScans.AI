from flask import Flask
from config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__, 
                template_folder='templates', 
                static_folder='static')
    app.config.from_object(config_class)

    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Import and register blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app 