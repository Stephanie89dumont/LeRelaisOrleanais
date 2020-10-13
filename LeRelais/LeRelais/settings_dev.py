"""local runserver settings"""
​
import os
from .settings import BASE_DIR
​
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y1$p&l05j8rbg%_se7^cc#5+35a!wkl()wek-x9tu*qm&9$9o3'

​
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
​
ALLOWED_HOSTS = []
​
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
​
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
