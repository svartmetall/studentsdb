import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': '1488',
        'NAME': 'students_db',
    }
}

EMAIL_HOST_USER = 'grongad'
EMAIL_HOST_PASSWORD = 'stalin1488'
ADMIN_EMAIL = 'grongad@gmail.com'
