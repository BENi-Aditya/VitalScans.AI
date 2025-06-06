import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'dcm'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') 