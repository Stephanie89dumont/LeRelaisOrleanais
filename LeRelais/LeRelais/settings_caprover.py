import os
from .settings import BASE_DIR
# key and debugging settings should not changed without care
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False
​
# allowed hosts get parsed from a comma-separated list
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")
​
​
# Database
DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.environ.get("DB_NAME"),
    "USER": os.environ.get("DB_USER"),
    "PASSWORD": os.environ.get("DB_PASSWORD"),
    "HOST": os.environ.get("DB_HOST"),
    "PORT": os.environ.get("DB_PORT"),
    }
}
