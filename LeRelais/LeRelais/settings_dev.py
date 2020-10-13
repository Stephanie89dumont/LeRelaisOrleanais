import os
from .settings import BASE_DIR

SECRET_KEY = "y1$p&l05j8rbg%_se7^cc#5+35a!wkl()wek-x9tu*qm&9$9o3"
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
