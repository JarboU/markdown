from django.conf.urls import url
from . import views
from django.conf.urls.static import static
import os
from django.conf import settings

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^uploadfile$', views.upload, name='upload'),
]

media_root = os.path.join(settings.BASE_DIR,'upload')
urlpatterns += static('/upload/', document_root=media_root)

