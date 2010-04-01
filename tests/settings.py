DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'tastypie.db'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'tastypie',
    'core',
]

ROOT_URLCONF = 'core.tests.api_urls'
