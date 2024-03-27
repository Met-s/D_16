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
________Изменил настройки ckeditor______
Без них пользователь аутентифицирован, но не авторизован для
доступа к этой странице создания и изменения страницы, то-есть текст написать
возможность есть, а добавить картинку и видео не получается.
Выдаёт ошибку сервера. "incorrect server response"
Что бы исправить нужно изменить:
bulletin/bulletin/urls.py

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

Вместо этого:
path('ckeditor/', include('ckeditor_uploader.urls')),

Добавить:
    path('ckeditor/upload/', login_required(ckeditor_views.upload),
         name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(
        ckeditor_views.browse)), name='ckeditor_browse'),
    path('posts/', include('board.urls')),
Всё работает!
___________Регистрация__________
Установил Allauth:
pip install django-allauth

В settings.py: добавляем настройки

В INSTALLED_APPS

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    Эти разделы должны уже быть:

    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',
----------
MIDDLEWARE = [
            ...
    'allauth.account.middleware.AccountMiddleware',
----------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
----------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
----------
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
----------
Проводим миграции
python manage.py migrate
----------
Настраиваем urls.py
bulletin/urls.py

path('accounts/', include("allauth.urls")),

Теперь если перейдём по ссылке:
http://127.0.0.1:8000/accounts/signup/
Попадём на страницу с формой для регистрации
----------
Чтобы форма регистрации отображалась в базовом шаблоне нужно в базовом шаблоне
allauth
venv/Lib/site-packages/allauth/templates/allauth/layouts/base.html

добавляем перенаправление на базовый шаблон default.html
{% extends "board/flatpages/default.html" %}
__________Кнопки в базовом шаблоне ВХОД, РЕГИСТРАЦИЯ И ВЫХОД______
В базовый шаблон default.html добавил кнопки.
Теперь если пользователь авторизован у него будет отображаться кнопка "ВЫХОД",
если не авторизован будут видны кнопки на "ВХОД" и "РЕГИСТРАЦИЮ".

{% if user.is_authenticated %}

                        <li class="nav-item active">
                                <a class="nav-link"
                                   href="/accounts/logout/">Выход
                                    <span class="sr-only"></span>
                                </a>
                        </li>
                    {% else %}
                        <li class="nav-item active">
                                <a class="nav-link" href="{% url 'account_login' %}">Вход
                                    <span class="sr-only"></span>
                                </a>
                        </li>
                        <li class="nav-item active">
                                <a class="nav-link" href="{% url 'account_signup' %}">Регистрация
                                    <span class="sr-only"></span>
                                </a>
                        </li>
                    {% endif %}

----------Другой вариант кнопок----------
                        <li>
                            {% if user.is_authenticated %}
                                <a href="{% url 'account_logout' %}"
                                   style="color: rgb(255, 255, 255);
                                   font-weight: 400;
                                   text-transform: uppercase;">ВЫХОД
                                </a>
                            {% else %}
                                <a href="{% url 'account_login' %}"
                                   style="color: rgb(255, 255, 255);
                                   font-weight: 400;
                                   text-transform: uppercase;">ВХОД
                                </a>
                                <a href="{% url 'account_signup' %}"
                                   style="color: rgb(255, 255, 255);
                                   font-weight: 400;
                                   text-transform: uppercase;">Регистрация
                                </a>
                            {% endif %}
                        </li>

_________Регистрация пользователя с подтверждением по email____
settings.py

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # количество дней для активации
ACCOUNT_USERNAME_MIN_LENGTH = 4     # минимальное количество символов логина
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend' # "dummy" или
    "console" будет крутиться в консоли, если "smtp" то отправляется на сервер

_______Настройки регистрации и авторизации allauth_____
 С подтверждением по email:
 settings.py

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # 'mandatory' -
# --------------
ACCOUNT_EMAIL_CONFIRMATION = 1
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_FORMS = {'signup': 'board.forms.CustomSignUpForm'}
# console, smtp
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('email_host_user')
EMAIL_HOST_PASSWORD = os.getenv('email_host_password')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv('default_from_email')

SERVER_EMAIL = os.getenv('server_email')

________Сокрытие личной информации "Паролей"_________
Устанавливаем python-dotenv
pip install python-dotenv
----------
Создаём текстовый файл в корневом каталоге проекта:

D_16\bulletin\.env
.env
Добавляем его в .gitignore

И записываем пароли
email_host_user = "пароль"
------------
В settings.py импортируем

import os
from dotenv import load_dotenv

load_dotenv()

Применим:
EMAIL_HOST_USER = os.getenv("email_host_user")

python-dotenv · PyPI
Подробнее здесь: https://pypi.org/project/python-dotenv/
==============================================================================
__________Удаление_commitov_______
Удалил коммиты с локального репо
git reset --soft <id_commit> -эта команда удаляет все коммиты после указанного
(а опция --soft сохраняет изменения)
push -не проходит если в коммите больше 100mb
==============================================================================

----------

----------

----------

----------

----------

----------

----------
