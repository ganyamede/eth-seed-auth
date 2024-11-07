import os

SECRET_KEY = os.getenv('SECRET_KEY')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_APPNAME = os.getenv('MONGO_APPNAME')

MONGO_URL = F"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@authweb3.5isui.mongodb.net/?retryWrites=true&w=majority&appName={MONGO_APPNAME}"