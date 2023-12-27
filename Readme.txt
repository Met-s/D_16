Установил  Ckeditor
pip install django-ckeditor
------настройки-ckeditor---
settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'board',
    'ckeditor',
    'ckeditor_uploader',
]
----------
STATIC_URL = 'static/'
STATIC_DIR = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOADER_PATH = "uploads/"
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'
----------запускаем команду для сбора статик файлов---
python manage.py collectstatic
----------

----------

----------





----------

----------

----------

----------

----------

----------

----------

----------

----------

----------
