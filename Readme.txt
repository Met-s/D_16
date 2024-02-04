Доска объявлений:

Регистрация:
    login, email
        код подтверждения на email
---
Объявления:
    заголовок,
    категории (Танки, Хилы, ДД, Торговцы, Гильдмастера, Квестгиверы, Кузнецы,
                Кожевники, Зельевары, Мастера заклинаний)
    текст (текст, картинка, видео, файл)
---
Пользователи:
    отправлять отклилки на объявления (текст)
        при отправке отклика пользователь должен получить email с оповещением
        о нём.
    приватная страница
        с откликами на его объявления
        внутри которой он может фильтровать отклики по объявлениям,
        удалять их и принимать (при принятии отклика, пользователю оставившему
                                отклик, также должно прийти уведомление)
---
Новостные рассылки на email

-------------------------------------------

---------------------------
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
Установка видео-плагина ckeditor html5.

Загружаем: https://ckeditor.com/cke4/addon/html5video
Подробно об установке и настройке здесь: https://devmaesters.com/blog/4

Копируем из загруженного архива папку html5video в
bulletin/static/ckeditor/ckeditor/plugins/

В board\urls.py добавляем

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
Файл будет выглядеть вот так:
urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('edit/<int:pk>/', PostUpdate.as_view(), name='edit_post'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

В settings.py добавляем настройки:

STATIC_URL = 'static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static/images')
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
CKEDITOR_BASE_PATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        # 'height': 300,   высота окна
        # 'width': 800,    ширина
        'removePlugins': 'exportpdf',
        'extraPlugins': ','.join(
            [
                'html5video',
            ]),
    },
}
Подробнее здесь:
https://django-ckeditor.readthedocs.io/en/latest/#plugins
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
