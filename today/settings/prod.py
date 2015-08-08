from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# Parse database cofiguration from $DATABASE_URL
import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
