import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    LINK_PER_PAGE = 8
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB limit for uploaded files
    UPLOAD_EXTENSIONS = ['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'webp']
    UPLOAD_PATH = os.path.join(basedir, 'uploads')