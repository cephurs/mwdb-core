import os

REDIS_DATABASE_URI = os.environ.get('REDIS_DATABASE_URI')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
CUCKOO2_API = os.environ.get('CUCKOO2_API')
SECRET_KEY = os.environ.get('SECRET_KEY')
UPLOAD_FOLDER = "/app/uploads/"
BASE_URL = os.environ.get("BASE_URL")
MAINTENANCE = os.environ.get("MAINTENANCE", False)
ENABLE_RATE_LIMIT = os.environ.get("ENABLE_RATE_LIMIT", False)
ENABLE_REGISTRATION = os.environ.get('ENABLE_REGISTRATION', False)
MAIL_SMTP = os.environ.get('MAIL_SMTP')
MAIL_FROM = os.environ.get('MAIL_FROM')
RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
RECAPTCHA_SECRET = os.environ.get('RECAPTCHA_SECRET')
