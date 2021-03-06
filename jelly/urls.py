from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^messapp/', include('messapp.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
