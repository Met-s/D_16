from django.urls import path
from .views import PostList, PostCreate, PostDetail, PostUpdate, PostDelete

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('edit/<int:pk>/', PostUpdate.as_view(), name='edit_post'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
