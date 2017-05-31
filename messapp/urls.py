from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
    # url(r'^profile/', 'profile', name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
