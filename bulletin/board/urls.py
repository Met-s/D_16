from django.urls import path
from .views import PostList, PostCreate, PostDetail

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = ([
    path('', PostList.as_view(), name='post_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
