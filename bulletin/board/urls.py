from django.urls import path
from .views import PostList

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = ([
    path('', PostList.as_view(), name='post_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
